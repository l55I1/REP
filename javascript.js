const nb_simulation = Math.pow(10, 6);
let nb_correct = 0;
for (let _ = 0; _ < nb_simulation; _++) {
    let x = Math.random();
    let y = Math.random();
    let z = Math.random();
    if ((x + y) + z === x + (y + z)) {
        nb_correct += 1;
    }
}
console.log((nb_correct / nb_simulation * 100).toFixed(2), "% accuracy for javascript");
