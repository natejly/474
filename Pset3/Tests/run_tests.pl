&sectionHeader('Verify');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('001', 'Small game, pure strategy');
$subtotal += &runTest('002', 'Small game, mixed strategy');
$subtotal += &runTest('003', 'Small game, optimize expected wins');
$subtotal += &runTest('004', 'Small game, not equilibrium');
$subtotal += &runTest('005', 'Bigger game, multiple equilibria');
$subtotal += &runTest('006', 'Bigger game, 2nd equilibrium');
$subtotal += &runTest('007', 'Bigger game, 3rd equilibrium');
$subtotal += &runTest('008', 'Bigger game, not an equilibrium');
$subtotal += &runTest('009', 'Bigger game, optimize wins');
$subtotal += &runTest('010', 'Bigger game, optimize wins; not an equilibrium');
$subtotal += &runTest('011', '10-unit game');
$subtotal += &runTest('012', '10-unit game, lottery scoring');
$subtotal += &runTest('013', '5-battlefield game');
$subtotal += &runTest('014', '5-battlefield game w/ memory limit');
$total += floor($subtotal);
&sectionResults('Verify', $subtotal, 14, $checkpoint );
$testCount += 14;

&sectionHeader('Finding equilibria');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('015', 'Small game, score');
$subtotal += &runTest('016', 'Small game, wins');
$subtotal += &runTest('017', 'Bigger game, score');
$subtotal += &runTest('018', 'Bigger game, lottery');
$subtotal += &runTest('019', 'Bigger game, wins');
$total += floor($subtotal);
&sectionResults('Finding equilibria', $subtotal, 5, $checkpoint );
$testCount += 5;

&sectionHeader('Tolerance');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('020', 'Higher tolerance, verify');
$subtotal += &runTest('021', 'Higher tolerance, find');
$subtotal += &runTest('022', 'Lower tolerance, find');
$total += floor($subtotal);
&sectionResults('Tolerance', $subtotal, 3, $checkpoint );
$testCount += 3;

