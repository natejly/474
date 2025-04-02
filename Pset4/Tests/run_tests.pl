&sectionHeader('MCTS');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('001', 'Cribbage Pegging Execution Test (succeeds if your program ran)');
$subtotal += &runTest('002', 'Kalah Execution Test (succeeds if your program ran)');
$total += floor($subtotal);
&sectionResults('MCTS', $subtotal, 2, $checkpoint );
$testCount += 2;

