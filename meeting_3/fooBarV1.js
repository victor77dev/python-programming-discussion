function fooBarV1(num) {
    console.log(`Foo Bar Game of ${num}`);
    for (let i = 1; i <= num; i++) {
        let output = '';
        if (i % 3 == 0) output += 'Foo';
        if (i % 5 == 0) output += 'Bar';
        if (i % 3 != 0 && i % 5 != 0) output += i.toString();
        console.log(output);
    }
}

fooBarV1(15);
fooBarV1(42);
fooBarV1(100);