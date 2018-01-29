var ExamApp = angular.module('ExamApp',['ui.router']);
ExamApp.config(["$interpolateProvider", function($interpolateProvider){
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
}]);
ExamApp.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/home');
	$stateProvider
        .state('comments',{
            url: '/comments',
            templateUrl: 'comments.html',
            controller: ''
        })
        .state('replies', {  
        	url: '/reply',
            templateUrl: 'partial-home.html',
            controller:   ''
        })
         .state('users',{
        	url: '/users/list',
            templateUrl: 'partial-home.html',
            controller: ''
        })
        .state('symptomslist',{
        	url: '/symptoms',
            templateUrl: 'partial-home.html',
            controller: ''
        })
        .state('medications',{
        	url: '/medications',
            templateUrl: 'partial-home.html',
            controller: ''
        })
        .state('exercises',{
        	url: '/exercises',
            templateUrl: 'partial-home.html',
            controller: ''
        })
        .state('restandrelaxation',{
        	url: '/restandrelaxation',
            templateUrl: 'partial-home.html',
            controller: ''
        })
         .state('foods',{
        	url: '/foods',
            templateUrl: 'partial-home.html',
            controller: ''
        })
          .state('reasons',{
        	url: '/reasons',
            templateUrl: 'partial-home.html',
            controller: ''
        });
});

