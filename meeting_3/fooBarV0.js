function fooBarV0(num) {
    console.log(`Foo Bar Game of ${num}`);
    for (let i = 1; i <= num; i++) {
        if (i % 15 == 0) {
            console.log('FooBar');
        } else if (i % 3 == 0) {
            console.log('Foo');
        } else if (i % 5 == 0) {
            console.log('Bar');
        } else {
            console.log(i);
        }
    }
}

fooBarV0(15);
fooBarV0(42);
fooBarV0(100);
