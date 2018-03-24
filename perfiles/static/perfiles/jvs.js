function mostrar_video(path_video){
	$(function() {
     // alert(pathVideo);
     $("#videoarea").attr({
		"src":  path_video,
		"poster": "",
		"autoplay": "autoplay"
     })
	})
}

function pintar_cuadro1(labelGraf3,datos3,titulo3){
	
	new Chart(document.getElementById("doughnut-chart"), {
                type: 'doughnut',
                data: {
                    labels: labelGraf3,
                    datasets: [{
                        label: "Estadisticas",
                        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                        data: datos3
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: titulo3
                    }
                }
            });
}

function pintar_cuadro2(labelGraf3,datos3,titulo3)
{
	 
     
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels:labelGraf3,
                    datasets: [{
                        label: titulo3,
                        data: datos3,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
}

function initMap() {
	var map;
    var myLatLng = {
        lat: -2.1843405,
        lng: -79.8770334
    };
    map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 14
    });
				
	var pos1 = {lat:-2.186040,lng:-79.876558}; //posicion del marcador
	addMarker(pos1,map,"Malecon","Sitio turistico Malecon 2000"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	var pos2 = {lat:-2.179344,lng:-79.875692}; //posicion del marcador
	addMarker(pos2,map,"Wyndham","Hotel Wyndham $143"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	var pos3 = {lat:-2.183074,lng:-79.877357}; //posicion del marcador
	addMarker(pos3,map,"Museo","Museo de los Bomberos"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	var pos4 = {lat:-2.183782,lng:-79.877464}; //posicion del marcador
	addMarker(pos4,map,"ESPOL","Universidad ESPOL"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	function addMarker(location, map,etiq,titulo) {
		var marker = new google.maps.Marker({
		position: location,
			title: titulo,
			label: etiq,
			map: map
		});
	
	
	 
	
		marker.addListener('click', function()
		{
			var pathVideo;
			var labelGraf;
			var datos;
			var datos1;
			var titulo;
			
			if (marker.label=="Malecon") {
                    pathVideo = "static/perfiles/videos/Malecon2000.mp4";
                    labelGraf = ["Visitas", "Diversiones", "Gastronomia", "Cines"];
                    datos     = [2478, 5267, 734, 784];
					datos1     = [5247, 3247, 1784, 2484];
                    titulo    = 'Estadisticas Malecon 2000 en el año 2018';

                   // alert(pathVideo);                  
                   }else if  (marker.label=="Wyndham"){
                    pathVideo = "static/perfiles/videos/Wyndham.webm";  
                    labelGraf = ["Hab. Simples", "Hab. Dobles", "Vista al Rio", "Internas"];
                    datos     = [400, 200,120, 200];
					datos1     = [300, 250,180, 220];
                    titulo    = 'Habitaciones en Hotel Wyndham'; 
                    //alert(pathVideo);                
                   
                  }else if  (marker.label== "Museo"){
                    pathVideo = "static/perfiles/videos/Museos.mp4"; 
                    labelGraf = ["Arte", "Cultura", "Antiguedades"];
                    datos     = [2000, 5267, 734];
					datos1     = [1300, 2467, 1534];
                    titulo    = 'Estadisticas de las Visitas en el Museo General de Guayaquil'; 
                    //alert(pathVideo);  
                   }else if (marker.label=="ESPOL") {
                    pathVideo =  "static/perfiles/videos/ESPOL.mp4";
                    labelGraf = ["Grado", "Posgrado", "Formación Continua", "Cisco"];
                    datos     = [5000, 1000, 500, 400];
					datos1     = [3000, 1500, 800, 2450];
                    titulo    = 'Número de Estudiantes en la ESPOL año 2018';

                    //alert(pathVideo);  

       }
	   else
	   {
                        pathVideo =  " ";
       }
	   mostrar_video(pathVideo);
	   pintar_cuadro1(labelGraf,datos,titulo);
	   pintar_cuadro2(labelGraf,datos1,titulo);
			
		});
	}
	
	//mostrar_video(pathVideo);
	//pintar_cuadro1("Espol");
	//pintar_cuadro2("Espol");
}