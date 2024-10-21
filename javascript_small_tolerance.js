const nb_simulation = Math.pow(10, 6);
results = [];

for (let t = 10; t < 21; t++) {
    let tolerance = Math.pow(10, -t);
    let nb_correct = 0;
    for (let _ = 0; _ < nb_simulation; _++) {
        let x = Math.random();
        let y = Math.random();
        let z = Math.random();
        if (((x + y) + z) - (x + (y + z)) < tolerance) {
            nb_correct += 1;
        }
    }
    results.push((nb_correct / nb_simulation * 100).toFixed(2));
    console.log(t, results.at(results.length - 1));
}

console.log("javascript", results.map((result) => {
    let res = result + "%";
    return " ".repeat(10 - res.length) + res;
}).join(""));