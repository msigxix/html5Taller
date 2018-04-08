var datos_c;
var datos_l;
var chart_c;
var chart_c1;

$(function() 
  {
    actualizar_cuadros("El Vecino");
		
    document.getElementById('removeData').addEventListener('click', function() {
		/*	datos_l.splice(-1, 1); // remove the label first
			datos_c.pop();*/
			chart_c.data.datasets.splice(0, 1);
			chart_c.update();
		});

		document.getElementById('removeData1').addEventListener('click', function() {
		/*	datos_l.splice(-1, 1); // remove the label first
			datos_c.pop();*/
			chart_c1.data.datasets.splice(0, 1);
			chart_c1.update();
		});		
  });
		

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

function pintar_cuadro1(labelGraf3,apro,repr,anul,reti,titulo3){
	
	chart_c1=new Chart(document.getElementById("doughnut-chart"), {
                type: 'doughnut',
                data: {
                    labels: labelGraf3,
                    datasets: [{
                        label: "Aprobados",
                        backgroundColor: ["red", "#8e5ea2", "yellow", "#e8c3b9", "#c45850"],
                        data: apro
                    },
					{label: "Reprobados",
                        backgroundColor: ["red", "#8e5ea2", "yellow", "#e8c3b9", "#c45850"],
                        data: repr},
					{label: "Anulados",
                        backgroundColor: ["red", "#8a5da2", "yellow", "#e8c3b9", "#c45850"],
                        data: anul},
					{label: "Retirados",
                        backgroundColor: ["red", "#8a5da2", "yellow", "#e8c3b9", "#c45850"],
                        data: reti
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


function pintar_cuadro2(labelGraf3,matri1,inscri1,prem1,titulo3)
{
	        var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels:labelGraf3,
                    datasets: [{
                        label: "Matriculados",
                        data: matri1,
                        backgroundColor: ['rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)'],
						borderColor:['rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)','rgba(255, 99, 132, 1)'] ,
                        borderWidth: 1
                    },
					{	
						label: "Inscritos",
                        data: inscri1,
						backgroundColor: ['rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)'],
						borderColor:['rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)','rgba(54, 162, 235, 1)'],
                        borderWidth: 1
					},
					{
						label: "Prematriculados",
                        data: prem1,
						backgroundColor: ['rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)'],
						borderColor:['rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)','rgba(255, 206, 86, 1)'],
                        borderWidth: 1
					}
					]
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
			chart_c=myChart;
}


function actualizar_cuadros(cuadro)
{
			var pathVideo;
			var labelGraf;
			var labelGraf1;
			var datos;
			var datos1;
			var titulo;
			var titulo1;
			var locacion;
			
			if (cuadro=="El Vecino") {
                    pathVideo = "static/perfiles/videos/Vecino.mp4";
                    labelGraf = ["Visitas", "Diversiones", "Gastronomia", "Cines"];
                    datos     = [2478, 5267, 734, 784];
					datos1     = [5247, 3247, 1784, 2484];
                    titulo    = 'UPS Cuenca - Campus El Vecino';
					titulo1 = 'UPS Cuenca - Campus El Vecino'
					locacion = 'El Vecino';

                   // alert(pathVideo);                  
                   }else if  (cuadro=="El Giron"){
                    pathVideo = "static/perfiles/videos/Giron.mp4";  
                    labelGraf = ["Hab. Simples", "Hab. Dobles", "Vista al Rio", "Internas"];
                    datos     = [400, 200,120, 200];
					datos1     = [300, 250,180, 220];
                    titulo    = '';
					titulo1    = '';
					locacion = 'El Giron';
                    //alert(pathVideo);                
                   
                  }else if  (cuadro== "Sur"){
                    pathVideo = "static/perfiles/videos/Sur.mp4"; 
                    labelGraf = ["Arte", "Cultura", "Antiguedades"];
                    datos     = [2000, 5267, 734];
					datos1     = [1300, 2467, 1534];
                    titulo    = 'UPS';
					titulo1    = 'UPS';
					locacion = 'Sur';
                    //alert(pathVideo);  
                   }else if (cuadro=="Centenario") {
                    pathVideo =  "static/perfiles/videos/Centenario.mp4";
                    labelGraf = ["Grado", "Posgrado", "Formación Continua", "Cisco"];
                    datos     = [5000, 1000, 500, 400];
					datos1     = [3000, 1500, 800, 2450];
                    titulo    = 'Número de Estudiantes en la ESPOL año 2018';
					titulo1='UPS Guayaquil - Campus Centenario'
					locacion = 'Centenario';
       }
	   else
	   {
                        pathVideo =  " ";
       }
	   var j=0;
	   var dat_mat=[];
	   var dat_ins=[];
	   var dat_pre=[];
	   
	   
	   labelGraf1=[];
	   for (i=0;i<campus.length;i++) {
		   if (campus[i]["cam_nombre"]==locacion)
		   {
			    dat_mat.push(matriculados[j]);
				dat_ins.push(inscritos[j]);
				dat_pre.push(prematriculados[j]);
				labelGraf1.push(carrera2[j]["car_nombre"]);
				j++;
		   }
		}
	   //alert(dat_mat);
	   j=0;
	   var dat_apro=[];
	   var dat_rep=[];
	   var dat_anu=[];
	   var dat_ret=[];
	   
	   
	   labelGraf=[];
	   for (i=0;i<campus1.length;i++) {
		   if (campus1[i]["cam_nombre"]==locacion)
		   {
			    dat_apro.push(aprobadas[j]);
				dat_rep.push(reprobados[j]);
				dat_anu.push(anulados[j]);
				dat_ret.push(retiros[j]);
				labelGraf.push(carrera1[j]["car_nombre"]);
				j++;
		   }
		}
	   
	   
	   
	   
	   mostrar_video(pathVideo);
	   pintar_cuadro1(labelGraf,dat_apro,dat_rep,dat_anu,dat_ret,'Rendimiento académico');
	   pintar_cuadro2(labelGraf1,dat_mat,dat_ins,dat_pre,'Estudiantes por Carrera');	
	   datos_c=datos1;
	   datos_l=labelGraf;
}

function initMap() {
	var map;
    var myLatLng = {
        lat: -1.6598254,
        lng: -74.8313854
    };
    map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 6
    });
				
	//var pos1 = {lat:-2.186040,lng:-79.876558}; //posicion del marcador
				
	var pos1 = {lat:-2.8863481,lng:-78.9914571}; //posicion del marcador
	addMarker(pos1,map,"El Vecino","UPS Cuenca - Campus El Vecino"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	//var pos2 = {lat:-2.179344,lng:-79.875692}; //posicion del marcador
    var pos2 = {lat:-0.2078324,lng:-78.4877541}; //posicion del marcador
    addMarker(pos2,map,"El Giron","UPS Quito - Campus El Girón"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	//var pos3 = {lat:-2.183074,lng:-79.877357}; //posicion del marcador
    var pos3 = {lat:-0.2825637,lng:-78.5500225}; //posicion del marcador
    addMarker(pos3,map,"Sur","UPS Quito - Campus Sur"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	//var pos4 = {lat:-2.183782,lng:-79.877464}; //posicion del marcador
    var pos4 = {lat:-2.5532183,lng:-79.7181717}; //posicion del marcador
    addMarker(pos4,map,"Centenario","UPS Guayaquil - Campus Centenario"); //añadimos el marcador con una etiqueta y un texto a mostrar de ayuda
				
	function addMarker(location, map,etiq,titulo1) {
		var marker = new google.maps.Marker({
		position: location,
			title: titulo1,
			label: etiq,
			map: map
		});
	
		marker.addListener('click', function()
		{
			actualizar_cuadros(marker.label);
		});
	}
	
	//mostrar_video("static/perfiles/videos/ESPOL.mp4");
	//pintar_cuadro1(["Grado", "Posgrado", "Formación Continua", "Cisco"],[5000, 1000, 500, 400],);
	//pintar_cuadro2(["Grado", "Posgrado", "Formación Continua", "Cisco"],[3000, 1500, 800, 2450],'Número de Estudiantes en la ESPOL año 2018');
}