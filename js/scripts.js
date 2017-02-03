function line(first,last,waiting,trip) {
  $('.firstStation').text(first);
  $('.lastStation').text(last);
  $('.meanWait').text(waiting);
  $('.trip').text(trip);
}


$('.lineA').click(function() {
  $('.firstStation').text('First station: San Pedrito');
  $('.lastStation').text('Last station: Plaza de Mayo');
  $('.meanWait').text('Mean waiting time: 3:21 minutes');
  $('.trip').text('Full trip duration: 26 minutes'); 
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineA.png");
});

$('.lineB').click(function() {
  $('.firstStation').text('First station: Juan Manuel de Rosas');
  $('.lastStation').text('Last station: Leandro N. Alem');
  $('.meanWait').text('Mean waiting time: 2:56 minutes');
  $('.trip').text('Full trip duration: 27 minutes');
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineB.png");
});

$('.lineC').click(function(){
  $('.firstStation').text('First station: Constitución');
  $('.lastStation').text('Last station: Retiro');
  $('.meanWait').text('Mean waiting time: 3:08 minutes');
  $('.trip').text('Full trip duration: 13 minutes');
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineC.png");
 });

$('.lineD').click(function(){
  $('.firstStation').text('First station: Congreso de Tucumán');
  $('.lastStation').text('Last station: Catedral');
  $('.meanWait').text('Mean waiting time: 3:04 minutes');
  $('.trip').text('Full trip duration: 26 minutes');
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineD.png");
 });
 
 $('.lineE').click(function(){
  $('.firstStation').text('First station: Plaza de los Virreyes');
  $('.lastStation').text('Last station: Bolivar');
  $('.meanWait').text('Mean waiting time: 6:01 minutes');
  $('.trip').text('Full trip duration: 24 minutes');
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineE.png");
 });
 
  $('.lineH').click(function(){
  $('.firstStation').text('First station: Hospitales');
  $('.lastStation').text('Last station: Las Heras');
  $('.meanWait').text('Mean waiting time: 6:31 minutes');
  $('.trip').text('Full trip duration: 24 minutes');
  $("#delayPlotId").attr("src","https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLineH.png");
 });
 
//$('.lineC').on('click', line('Constitucion','Retiro','4 min','22 min'))