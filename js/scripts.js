
//subway data object
var subteInfoObj = {
  A:{
    firstStation: 'San Pedrito',
    lastStation: 'Plaza de Mayo',
    meanWait: '3:21',
    trip: '26'  
  },
  B:{
    firstStation: 'Juan Manuel de Rosas',
    lastStation: 'Leandro N. Alem',
    meanWait:'2:56',
    trip:'27'  
  },
  C:{
    firstStation: 'Constitución',
    lastStation: 'Retiro',
    meanWait:'3:08',
    trip:'13'  
  },
  D:{
    firstStation: 'Congreso de Tucumán',
    lastStation: 'Catedral',
    meanWait:'3:04',
    trip:'26'  
  },
  E:{
    firstStation: 'Plaza de los Virreyes',
    lastStation: 'Bolivar',
    meanWait:'6:01',
    trip:'24'  
  },
  H:{
    firstStation: 'Hospitales',
    lastStation: 'Las Heras',
    meanWait:'6:31',
    trip:'24'  
  }  
}

//Function to load data
function lineInfo(line) {
  //return subteInfoObj.call(line)
  
  $('.firstStation').text('First station FLAG: ' + subteInfoObj[line].firstStation);
  $('.lastStation').text('Last station FLAG: ' + subteInfoObj[line].lastStation);
  $('.meanWait').text('Mean waiting time: ' + subteInfoObj[line].meanWait +' minutes');
  $('.trip').text('Full trip duration: ' + subteInfoObj[line].trip + ' minutes');
  $("#delayPlotId").attr("src",'https://raw.githubusercontent.com/alephcero/baSubwayObservatory/master/img/plotLine'+line+'.png'); 
}


// Button funcionality
$('.lineA').on('click',lineInfo('A'));
$('.lineB').on('click',lineInfo('B'));
$('.lineC').on('click',lineInfo('C'));
$('.lineD').on('click',lineInfo('D'));
$('.lineE').on('click',lineInfo('E'));
$('.lineH').on('click',lineInfo('H'));

