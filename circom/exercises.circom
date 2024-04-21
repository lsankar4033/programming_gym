/*
 Various exercises for learning
 */
pragma circom 2.0.0;

template Num2Bits(n) {
    signal input in;
    signal output out[n];
    var lc1=0;

    var e2=1;
    for (var i = 0; i<n; i++) {
        out[i] <-- (in >> i) & 1;
        out[i] * (out[i] -1 ) === 0;
        lc1 += out[i] * e2;
        e2 = e2+e2;
    }

    lc1 === in;
}

template LessThan(n) {
    assert(n <= 252);
    signal input in[2];
    signal output out;

    component n2b = Num2Bits(n+1);

    n2b.in <== in[0]+ (1<<n) - in[1];

    out <== 1-n2b.out[n];
}

// N is the number of bits the input  have.
// The MSF is the sign bit.
template LessEqThan(n) {
    signal input in[2];
    signal output out;

    component lt = LessThan(n);

    lt.in[0] <== in[0];
    lt.in[1] <== in[1]+1;
    lt.out ==> out;
}

template QuinSelector(n) {
  signal input in[n];
  signal input idx;
  signal output out;
  signal tmp;

  tmp <-- in[idx];

  // constraints:
  // - idx < n
  // - idx > 0
  // - tmp === out

  out <== tmp;

  // this can't be good practice
  component le = LessThan(252);
  le.in[0] <== idx;
  le.in[1] <== n;
  le.out === 1;

  component leq = LessEqThan(252);
  leq.in[0] <== 0;
  leq.in[1] <== idx;
  leq.out === 1;
}

component main = QuinSelector(10);
