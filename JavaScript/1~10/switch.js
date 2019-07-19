var rank = 'B';

switch (rank) {
    case 'A':
        console.log('A');
        break;
    case 'B':
        console.log('B');
        break;
    case 'C':
        console.log('C');
        break;
    default:
        console.log('該当なし');
        break;
}

switch (rank) {
    case 'A':
    case 'B':
    case 'C':
        console.log('合格')
    case 'D':
        console.log('不合格')
    default:
        break;
}