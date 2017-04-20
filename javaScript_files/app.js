var matrix = [
	['Tamano de Empresa', 'Banamex', 'Banorte/Ixe', 'BBVA Bancomer', 'HSBC', 'Inbursa', 'Santander', 'Scotiabank'], 
	['Micro', 12335462070.0, 13250078208.0, 67111422990.0, 4742027084.0, 1562328989.0, 45152195198.0, 1981181472.0], 
	['Pequena', 36193751812.0, 28657275248.0, 29250420914.0, 7202320549.0, 1914211506.0, 37036315651.0, 4756875161.0], 
	['Mediana', 8806189580.0, 7283777521.0, 12672115631.0, 3024407852.0, 824189253.0, 11240244966.0, 3780298351.0], 
	['Grande', 185125000000.0, 149911000000.0, 309959000000.0, 123377000000.0, 129385000000.0, 197667000000.0, 84533374284.0], 
	['Fideicomiso', 1077562167.0, 8246492359.0, 5200903257.0, 1930724990.0, 43575401372.0, 3049737277.0, 1795836142.0]
]

var chart_array = [
	['Banco', '201612'], 
	['Banamex', 243537965629.0], 
	['Banorte/Ixe', 200064845815.0], 
	['BBVA Bancomer', 424193862792.0], 
	['HSBC', 12157453391.0], 
	['Inbursa', 177261131120.0], 
	['Santander', 294145493092.0], 
	['Scotiabank', 96847565410.0]
]



function transpose_matrix(matrix){
  var newArray = [],
    origArrayLength = matrix.length,
    arrayLength = matrix[0].length,
    i;
  
  for(i = 0; i < arrayLength; i++){
      newArray.push([]);
  };

  for(i = 0; i < origArrayLength; i++){
      for(var j = 0; j < arrayLength; j++){
          newArray[j].push(matrix[i][j]);
      };
  };
  return newArray  
};


function SumChartRow(chart_row){
	var row_total = 0
	for (var i = chart_row.length - 1; i > 0; i--) {
		row_total += chart_row[i]
	}
	return row_total
};


function SortChartArray(chart_array){
		
	var old_array = chart_array.slice()
	var sorted_array = [old_array.shift()]

	old_array.sort(function (a, b) {	  
	  return SumChartRow(b) - SumChartRow(a);
	});

	return sorted_array.concat(old_array)
}

console.log(SortChartArray(chart_array))
// console.log(' ')
// console.log(chart_array)

// console.log(['a'].concat(['b']))

