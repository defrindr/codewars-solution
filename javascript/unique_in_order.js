function unique_order(lst) {
    console.log(Array.from(new Set(lst)));
}

unique_order(['a', 'b', 'b', 1, 2, 1, 2, 'c', 'c', 'c', 'c', 'd']);