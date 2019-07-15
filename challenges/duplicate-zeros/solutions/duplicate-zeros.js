function duplicateZeros(array) {
  let length = array.length;
  for (i = 0; i < array.length; i++) {
    if (array[i] === 0) {
      i++;
      array.splice(i - 1, 0, 0);
      array.length = length;
    }
  }
  //console.log(array)
}
