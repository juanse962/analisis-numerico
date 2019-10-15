var m1 = [[5]];
var m2 = [[1, 2], [3, 4]];
var m3 = [[1, 2, 1], [1, 2, 3], [-1, 3, 3]];
var m4 = [[1, 2, 1, 2], [1, 2, 3, 4], [-1, 3, 3, -1], [2, 2, 1, 1]];
var m5 = [
  [1, 2, 1, 2, 1],
  [1, 2, 3, 4, 2],
  [-1, 13, 3, -1, 3],
  [2, 2, 1, 1, 4],
  [1, 2, 3, 4, 5]
];
var m6 = [
  [1, 2, 1, 2, 1, 6],
  [1, 2, 3, 4, 2, 7],
  [-1, 13, 3, -1, 3, 8],
  [2, 2, 1, 1, 4, 9],
  [1, 2, 3, 4, 5, 10],
  [6, 7, 8, 9, 10, 11]
];

let determinante2 = matrix => {
  return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1];
};

let determinanteRecursivo = (matrix, elemento = 1) => {
  let n = matrix.length;
  if (n === 1) {
    return matrix[0][0];
  } else if (n === 2) {
    return elemento * determinante2(matrix);
  } else {
    let signo = -1;
    var suma = 0;
    for (let i = 0; i < n; i++) {
      let temp = matrix.map(val => val.slice(1, n));
      temp.splice(i, 1);
      signo *= -1;
      suma += signo * determinanteRecursivo(temp, matrix[i][0]);
    }
    return suma * elemento;
  }
};

console.table(m1);
console.log('Determinante', determinanteRecursivo(m1));

console.table(m2);
console.log('Determinante', determinanteRecursivo(m2));

console.table(m3);
console.log('Determinante', determinanteRecursivo(m3));

console.table(m4);
console.log('Determinante', determinanteRecursivo(m4));

console.table(m5);
console.log('Determinante', determinanteRecursivo(m5));

console.table(m6);
console.log('Determinante', determinanteRecursivo(m6));


