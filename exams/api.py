from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import logging
from rest_framework.response import Response
from rest_framework import status
from . import permissions

logger = logging.getLogger('django.request')


# question api
class QuestionListView(ListAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (permissions.AdminPermission,)


class QuestionView(APIView):
    permission_classes = (permissions.AdminPermission,)

    def get_object(self, pk):
        try:
            print('inside get try')
            return models.Question.objects.get(pk=pk)
        except models.Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            code = status.HTTP_201_CREATED
            status_message = "Success"
            return Response(serializer.data, code, status_message)
        return Response(serializer.errors, self.code, self.status_message)

    def put(self, request, pk):
        try:
            question = self.get_object(pk)
            serializer = serializers.QuestionSerializer(question, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                code = status.HTTP_200_OK
                status_message = "Success"
                return Response(serializer.data, code, status_message)
        except Exception as e:
            logger.error(repr(e))
            # return Response(serializer.errors,code,status_message)

    def delete(self, request, pk):
        try:
            question = self.get_object(pk)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Exam.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # logger.error(repr(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    permission_classes = (permissions.AdminStudentPermission,)

    def get_object(self, pk):
        try:
            print('inside get try')
            return models.Question.objects.get(pk=pk)
        except models.Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        try:
            question = self.get_object(pk)
            serializer = serializers.QuestionSerializer(question)
            code = status.HTTP_200_OK
            status_message = "Success"
            return Response(serializer.data, code, status_message)
        except Exception as e:
            logger.error(repr(e))
            # return Response(serializer.errors, code, status_message)


# exam API
class ExamListView(ListAPIView):
    queryset = models.Exam.objects.all()
    serializer_class = serializers.ExamSerializer
    permission_classes = (permissions.AdminStudentPermission,)


class ExamView(APIView):
    code = status.HTTP_400_BAD_REQUEST
    status_message = "Failed"
    permission_classes = (permissions.AdminPermission,)

    def get_object(self, pk):

        print("inside exam get object")
        return models.Exam.objects.get(pk=pk)

    def post(self, request):
        serializer = serializers.ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            code = status.HTTP_201_CREATED
            status_message = "Success"
            return Response(serializer.data, code, status_message)
        return Response(serializer.errors, self.code, self.status_message)

    def put(self, request, pk):
        try:
            exam = self.get_object(pk)
            serializer = serializers.ExamSerializer(exam, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                code = status.HTTP_200_OK
                status_message = "Success"
                return Response(serializer.data, code, status_message)
        except Exception as e:
            logger.error(repr(e))

    def get(self, request, pk, format=None):
        try:
            exam = self.get_object(pk)
            serializer = serializers.ExamSerializer(exam)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.Exam.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(repr(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            exam = self.get_object(pk)
            exam.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Exam.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Response api
class ResponseListView(ListAPIView):
    queryset = models.Response.objects.all()
    serializer_class = serializers.ResponseListSerializer
    permission_classes = (permissions.AdminPermission,)


class ResponseView(APIView):
    permission_classes = (permissions.AdminStudentPermission,)

    def get_object(self, pk):
        try:
            return models.Response.objects.get(pk=pk)
        except models.Response.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        print("inside response create")
        serializer = serializers.ResponseSerializer(data=request.data)
        print(request.data)
        print("inside response create 2")
        data=dict()
        if serializer.is_valid():
            print("inside response create3")
            try:
                # data.update
                serializer.save(user=request.user)
                # data = request.data.copy()
                # models.Response(
                #     response_field=data.get('response_field',None),
                # ).save()
                print("inside response create4")
                # code = status.HTTP_201_CREATED
                print("inside response create 5")
                # status_message = "Success"
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(repr(e))
                # else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            response = self.get_object(pk)
            serializer = serializers.ResponseSerializer(response, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                code = status.HTTP_200_OK
                status_message = "Success"
                return Response(serializer.data, code, status_message)
        except Exception as e:
            logger.error(repr(e))

    def delete(self, request, pk):
        try:
            response = self.get_object(pk)
            response.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Response.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(repr(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ResponseDetailView(APIView):
    permission_classes = (permissions.AdminPermission,)

    def get_object(self, pk):
        try:
            return models.Response.objects.get(pk=pk)
        except models.Response.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            response = self.get_object(pk)
            serializer = serializers.ResponseSerializer(response)
            code = status.HTTP_200_OK
            status_message = "Success"
            return Response(serializer.data, code, status_message)
        except Exception as e:
            logger.error(repr(e))
