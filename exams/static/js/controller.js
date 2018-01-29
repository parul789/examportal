ExamApp.controller("ExamController",["$scope","$http",function($scope,$http){
    var token = 'Token t';
    $scope.questionList = function(){
		console.log('in questionlist function');
		$http({
			method:'GET',
		    url:'/questions/',
		    headers:{
				'Content-Type':'application/json',
				'Authorization': token
		},
		}).then(function successCallback(response){
		console.log(response);
		$scope.questions=response.data;
        },function errorcallback(response){
		console.log("error");
		console.log(response);
	});
	};

	$scope.questionEdit = function(id){
	    console.log('in questionedit function');
	    $http({
	    method : 'PUT',
        url : '/questions/edit/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.question,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};




	$scope.questionCreate = function(){
	    console.log('in questionCreate function');
	    $http({
	    method : 'POST',
        url : '/questions/create/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.question,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.get_id = function(id){
	    console.log(id);
	    $scope.edit_id = id;
	    $scope.symptomsDetail(id);
	};

    $scope.questionDetail = function(id){
	    console.log('in questionDetail function');
	    $http({
	    method : 'GET',
        url : '/questions/detail/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        $scope.question = response.data;
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.questionsDelete = function(id){
	    console.log('in questionsDelete function');
	    $http({
	    method : 'DELETE',
        url : '/questions/delete/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        $window.location.reload();
//        $scope.symptomsList();
        },function errorcallback(response){
        console.log(response);
        console.log("error");
        });
	};

    $scope.ExamList = function(){
		console.log('in ExamList function');
		$http({
			method:'GET',
		    url:'/exams/',
		    headers:{
				'Content-Type':'application/json',
				'Authorization': token
		},
		}).then(function successCallback(response){
		console.log(response);
		$scope.exam=response.data;
        },function errorcallback(response){
		console.log("error");
		console.log(response);
	});
	};

	$scope.medicationsnextlist = function(next){
	   $http({
			method:'GET',
		    url:next,
		    headers:{
				'Content-Type':'application/json',
				'Authorization': token
		},
		}).then(function successCallback(response){
		console.log(response);
		$scope.medications=response.data;
        },function errorcallback(response){
		console.log("error");
		console.log(response);
		console.log(next);
	});
	};

	$scope.medicationspreviouslist = function(prev){
	   $http({
			method:'GET',
		    url:prev,
		    headers:{
				'Content-Type':'application/json',
				'Authorization': token
		},
		}).then(function successCallback(response){
		console.log(response);
		$scope.medications=response.data;
        },function errorcallback(response){
		console.log("error");
		console.log(response);
	});
	};

	$scope.examEdit = function(id){
	    console.log('in examEdit function');
	    $http({
	    method : 'PUT',
        url : '/exams/edit/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.exam,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.examsCreate = function(){
	    console.log('in examsCreate function');
	    $http({
	    method : 'POST',
        url : '/exams/create/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.exam,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

    $scope.examDetail = function(id){
	    console.log('in examDetail function');
	    $http({
	    method : 'GET',
        url : '/exams/detail/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.examDelete = function(id){
	    console.log('in examDelete function');
	    $http({
	    method : 'DELETE',
        url : '/exams/delete/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

    $scope.responsesList = function(){
		console.log('in responsesList function');
		$http({
			method:'GET',
		    url:'/responses/',
		    headers:{
				'Content-Type':'application/json',
				'Authorization': token
		},
		}).then(function successCallback(response){
		console.log(response);
		$scope.responses = response.data;
        },function errorcallback(response){
		console.log("error");
		console.log(response);
	});
	};


	$scope.responsesEdit = function(id){
	    console.log('in responsesEdit function');
	    $http({
	    method : 'PUT',
        url : '/responses/edit/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.responses,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.responsesCreate = function(){
	    console.log('in responsesCreate function');
	    $http({
	    method : 'POST',
        url : '/responses/create/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        data: $scope.responses,
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

    $scope.responsesDetail = function(id){
	    console.log('in responsesDetail function');
	    $http({
	    method : 'GET',
        url : '/responses/detail/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};

	$scope.responsesDelete = function(id){
	    console.log('in responsesDelete function');
	    $http({
	    method : 'DELETE',
        url : '/responses/delete/'+id+'/',
        headers : {
                'Content-Type':'application/json',
                'Authorization':token
        },
        }).then(function successCallback(response){
        console.log(response);
        },function errorcallback(response){
        console.log('response');
        console.log("error");
        });
	};
}]);

