app.config(function($routeProvider) {
        $routeProvider

            // route for the home page
            .when('/', {
                templateUrl : '/list/view/',
               	controller  : 'listController'

            }).when('/filemanager/import/csv/view/', {
                templateUrl : '/filemanager/import/csv/view/',
               	controller  : 'fileController'

            }).when('/catalog/view/products/', {
                templateUrl : '/catalog/view/products/',
               	controller  : 'catalogController'

            })
            .when('/list/create/', {
                templateUrl : '/list/create/',
                controller  : 'listController'

            })
            .when('/list/view/', {
                templateUrl : '/list/view/',
                controller  : 'listController'

            }).
      otherwise({
        templateUrl : '/filemanager/import/csv/view/',
        controller  : 'fileController'
      });

            
            
    });

app.controller('fileController', ['$scope', 'defaultService', function ($scope, defaultService) {
$scope.estado = "Seleccione un archivo";
$scope.descargar_csv = function(){
  console.log("downloading csv method "+$scope.nombre);
  
	if ($scope.nombre === undefined){
		$scope.estado = "El nombre no puede estar vacio"
	}

	else{
	     $scope.estado = "Descargando archivo";  
		    defaultService.get('/filemanager/csv/download/?file='+$scope.nombre, function(d){
		    $scope.estado = "Importando archivo";
        defaultService.get('/filemanager/import/csv/action/', function(d){
            //console.log(d)
        //alert(d);
        $scope.estado = d;
                               }, function (e){console.log("error:"+e);}
        );
		    

		       										 }, function (e){console.log("error:"+e);}
		    );
	    }  
    }  


$scope.import_repo = function(repo){
  console.log(repo);
  $scope.estado = "Descargando archivo";
  //alert("Descargando archivo");
  defaultService.get('/filemanager/csv/download/?file='+repo, function(d){
        
        $scope.estado = "Importando archivo";
        defaultService.get('/filemanager/import/csv/action/', function(d){
            //console.log(d)
        //alert(d);
        $scope.estado = d;
                               }, function (e){console.log("error:"+e);}
        );
        //alert(d);
                                                            }, function (e){console.log("error:"+e);}
        );
}




}]);



app.controller('catalogController', ['$scope', 'defaultService', function ($scope, defaultService) {
  defaultService.get('/catalog/get/json/', function(d){
            console.log(d)
        $scope.products = d;    
        console.log($scope.products);
                               }, function (e){console.log("error:"+e);}
        );
}]);



app.controller('listController', ['$scope', 'defaultService', function ($scope, defaultService) {
 
 //initial values
  $("#action_container").css("display", "none");
  $scope.lists = [];
  $scope.products_preview = [];
 //initial values

//list lists view 
  defaultService.get('/list/service/', function(d){
            $scope.lists = d;
            //console.log($scope.lists);
                  }, function (e){console.log("error:"+e);}
        );


   $scope.products_list = function(list_id){
      $("#action_container").css("display", "inline");
      var index = parseInt(list_id[0]);     
      
      
      //console.log($scope.lists[index].productos);
      //console.log(JSON.parse($scope.lists[index].productos));
      $scope.products_list_aux = JSON.parse($scope.lists[index].productos) ;
      $scope.current_list = JSON.parse($scope.lists[index].pk)
      $scope.current_list_name = $scope.lists[index].name;
      //console.log($scope.current_list);
  }

 $scope.add_product = function(product){
    console.log($scope.products_list_aux);
    console.log(product);
    for(prod in $scope.products_list_aux){
        
        if($scope.products_list_aux[prod].sku === product.sku){
          alert("producto ya incluido");
          return;
        }
      }
    $("#btn-grabar").prop('disabled', false);
    $scope.products_list_aux.push(product);
  }   

  $scope.delete_product = function(product_sku){
      var index = 0;
      for(prod in $scope.products_list_aux){
        
        if($scope.products_list_aux[prod].sku === product_sku){
                 
          $scope.products_list_aux.splice($scope.products_list_aux.indexOf($scope.products_list_aux[prod]),1);
          var data = {};
          data['list_pk'] = $scope.current_list;
          data['products'] = $scope.products_list_aux;
          defaultService.put('/list/service/',data, function(d){
          alert("Lista editada con exito")
          $scope.lists = d;
            //$scope.lists = d;
                  }, function (e){console.log("error:"+e);}
              );
          return ;
        }
      }

      console.log(index);
  } 


  $scope.delete_list = function(pk){
   defaultService.delete('/list/service/'+pk+'/', function(d){
    alert("Lista eliminada con exito")
            $scope.lists = d;
                  }, function (e){console.log("error:"+e);}
        );
  }

  $scope.save_edited_list = function(){
    var data = {};
    data['list_pk'] = $scope.current_list;
    data['products'] = $scope.products_list_aux;
    console.log(data);
    defaultService.put('/list/service/',data, function(d){
    alert("Lista editada con exito")
    $scope.lists = d;
            //$scope.lists = d;
                  }, function (e){console.log("error:"+e);}
        );
  }

//list lists view 
  
 

 


//create list view
 $scope.search = function(){
      console.log($scope.texto);
      
      var params = $scope.texto.split(" ");
      console.log(params);
      console.log(params.length);
      if(params.length > 5){
        alert("El numero de palabras debe ser menor a 5");
      }
      else{
        $(".loading").css("display","inline");
        defaultService.get('/catalog/service/search/?tag='+$scope.texto, function(d){
        console.log(d)
        $scope.products = d; 
        $(".loading").css("display","none");

        console.log($scope.products);
                               }, function (e){console.log("error:"+e);}
        );
      }
      
    }



  $scope.include_product = function(p){
    //console.log(p);
    //console.log($scope.products_preview.length);
    $("#list-name").prop('disabled', false);
    $("#btn-grabar").prop('disabled', false);
    
    if($scope.products_preview.length === 0){
      $scope.products_preview.push(p);
    }
    else{
      console.log(p.sku);
      for(prod in $scope.products_preview){
        
        if($scope.products_preview[prod].sku === p.sku){
          alert("producto ya incluido");
          return;
        }
      }
      $scope.products_preview.push(p);
    }
    
    
    
    
  }

  $scope.save_list = function(){

    var data = {};
    data['name'] = $scope.list_name;
    data['products'] = $scope.products_preview;
    defaultService.post('/list/service/',data, function(d){
            console.log(d)
        alert(d) 
        console.log($scope.products);
                               }, function (e){console.log("error:"+e);}
        );

  }
//list lists view 


  





}]);

