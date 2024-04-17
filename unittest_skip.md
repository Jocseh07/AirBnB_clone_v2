to skip a test, use the skip() decorator
use the TestCase.skipTest() within a setUp()
or raising SkipTest directly

so for exanple
@unittest.skip("demonstrating skipping")
def test_nothing(self):
self.fail("shouldn't happen")

another is using the sskip if
@unittest.skipIf(mylib.**version**< (1, 3), "not supported in this library version)
def test_format(self):
pass

@unittest.skipUnless(sys.platform.startswith9'win"), "requires Windows"
def test_windows_support(self);
always skips unless true

def test_maybe_skipped(self):
self.skipTest("external resource not available")
pass

classes can be skipped like methods
@unittest.skip("")
class

testcase.setUp can also skip the test

expected failures use the expectedFailure() decorator

it is easy to roll your own skipping decorators by making a decorator that calls skip() on the test when it wants it to be skipped
this decorator skips the test unless the pased object has a certain attribute

return unittest.skip("")
