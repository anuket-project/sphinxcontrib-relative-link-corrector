#!/bin/bash

set -o errexit
set -o nounset
set -x

srcDir="testproject"
outDir="build-sphinx-testproject"

echo "Building 'testproject' with postpocessing disabled..."
rm -rf "$outDir"
sphinx-build -T -vvv -b html -D language=en "$srcDir" "$outDir"

echo "[runtest.sh] Checking negative corrections"
[ "$(grep -c 'href="https://github.com/cntt-n/relative-link-corrector/linked.html">link 3</a>' $outDir/index.html || true)" = "0" ]
[ "$(grep -c 'href="https://github.com/cntt-n/relative-link-corrector/linked.html#anchor">'    $outDir/index.html || true)" = "0" ]

echo "[runtest.sh] Check positive corrections"
[ "$(grep -c 'href="linked.html">'                                                             $outDir/index.html || true)" = "1" ]
[ "$(grep -c 'href="linked.html#anchor">'                                                      $outDir/index.html || true)" = "1" ]
#[ "$(grep -c 'href="https://github.com/cntt-n/relative-link-corrector/linked.md">link 3</a>'  $outDir/index.html || true)" = "1" ]
[ "$(grep -c 'href="https://github.com/cntt-n/relative-link-corrector/linked.md#anchor">'      $outDir/index.html || true)" = "1" ]

echo "[runtest.sh] All tests passed."
