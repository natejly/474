&sectionHeader('Cribbage Pegging (40 points)');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('001', '0.01 seconds', 'grep "NET_PEG-4_01" scores | cut -d\';\' -f1 | cut -d\' \' -f2 | python3 ~/Common/assess_average.py --mean --inflection -10.0 -2.0 -0.45 -0.26 -0.04 --score 0 60 80 90 100');
$subtotal += &runTest('002', '0.05 seconds', 'grep "NET_PEG-4_05" scores | cut -d\';\' -f1 | cut -d\' \' -f2 | python3 ~/Common/assess_average.py --mean --inflection -10.0 -2.0 -0.22 -0.08 -0.03 --score 0 180 240 270 300');
$total += floor($subtotal);
&sectionResults('Cribbage Pegging (40 points)', $subtotal, 2, $checkpoint );
$testCount += 2;

&sectionHeader('5-card Cribbage Pegging (20 points)');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('003', '0.01 seconds', 'grep "NET_PEG-5_01" scores | cut -d\';\' -f1 | cut -d\' \' -f2 | python3 ~/Common/assess_average.py --mean --inflection -10.0 -3.0 -0.60 -0.16 0.20 --score 0 60 80 90 100');
$subtotal += &runTest('004', '0.05 seconds', 'grep "NET_PEG-5_05" scores | cut -d\';\' -f1 | cut -d\' \' -f2 | python3 ~/Common/assess_average.py --mean --inflection -10.0 -3.0 0.04 0.17 0.25 --score 0 60 80 90 100');
$total += floor($subtotal);
&sectionResults('5-card Cribbage Pegging (20 points)', $subtotal, 2, $checkpoint );
$testCount += 2;

&sectionHeader('Kalah (40 points)');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &runTest('005', '0.1 seconds', 'grep "NET_KALAH_10" scores | cut -d\';\' -f2 | cut -d\' \' -f3 | python3 ~/Common/assess_average.py --mean --inflection 0.0 0.10 0.30 0.40 0.64 --score 0 60 80 90 100');
$subtotal += &runTest('006', '0.5 seconds', 'grep "NET_KALAH_50" scores | cut -d\';\' -f2 | cut -d\' \' -f3 | python3 ~/Common/assess_average.py --mean --inflection 0.0 0.10 0.38 0.56 0.72 --score 0 180 240 280 300');
$total += floor($subtotal);
&sectionResults('Kalah (40 points)', $subtotal, 2, $checkpoint );
$testCount += 2;

&sectionHeader('Convert From 0-1000 to 0-100');
$subtotal = 0;
@SOURCE = ();
@LINK = ();
$subtotal = &failTest('007', 'Dummy Test (will fail)');
$subtotal = $subtotal * 0 / 1;
$total = floor($total / 10);
$total += floor($subtotal);
&sectionResults('Convert From 0-1000 to 0-100', $subtotal, 1, $checkpoint );
$testCount += 1;

