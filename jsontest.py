#!/usr/bin/python

## this test suite is an almost verbatim copy of the jsontest.py test suite
## found in json-py available from http://sourceforge.net/projects/json-py/
##
## Copyright (C) 2005  Patrick D. Logan
## Contact mailto:patrickdlogan@stardecisions.com
##
## This library is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public
## License as published by the Free Software Foundation; either
## version 2.1 of the License, or (at your option) any later version.
##
## This library is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public
## License along with this library; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import unittest

import cjson
_exception = cjson.DecodeError

# The object tests should be order-independent. They're not.
# i.e. they should test for existence of keys and values
# with read/write invariance.

def _removeWhitespace(str):
    return str.replace(" ", "")

class JsonTest(unittest.TestCase):
    def testReadEmptyObject(self):
        obj = cjson.decode("{}")
        self.assertEqual({}, obj)

    def testWriteEmptyObject(self):
        s = cjson.encode({})
        self.assertEqual("{}", _removeWhitespace(s))

    def testReadStringValue(self):
        obj = cjson.decode('{ "name" : "Patrick" }')
        self.assertEqual({ "name" : "Patrick" }, obj)

    def testReadEscapedQuotationMark(self):
        obj = cjson.decode(r'"\""')
        self.assertEqual(r'"', obj)

#    def testReadEscapedSolidus(self):
#        obj = cjson.decode(r'"\/"')
#        self.assertEqual(r'/', obj)

    def testReadEscapedReverseSolidus(self):
        obj = cjson.decode(r'"\\"')
        self.assertEqual("\\", obj)

    def testReadEscapedBackspace(self):
        obj = cjson.decode(r'"\b"')
        self.assertEqual("\b", obj)

    def testReadEscapedFormfeed(self):
        obj = cjson.decode(r'"\f"')
        self.assertEqual("\f", obj)

    def testReadEscapedNewline(self):
        obj = cjson.decode(r'"\n"')
        self.assertEqual("\n", obj)

    def testReadEscapedCarriageReturn(self):
        obj = cjson.decode(r'"\r"')
        self.assertEqual("\r", obj)

    def testReadEscapedHorizontalTab(self):
        obj = cjson.decode(r'"\t"')
        self.assertEqual("\t", obj)

    def testReadEscapedHexCharacter(self):
        obj = cjson.decode(r'"\u000A"')
        self.assertEqual("\n", obj)
        obj = cjson.decode(r'"\u1001"')
        self.assertEqual(u'\u1001', obj)

    def testWriteEscapedQuotationMark(self):
        s = cjson.encode(r'"')
        self.assertEqual(r'"\""', _removeWhitespace(s))

    def testWriteEscapedSolidus(self):
        s = cjson.encode(r'/')
        #self.assertEqual(r'"\/"', _removeWhitespace(s))
        self.assertEqual('"/"', _removeWhitespace(s))

    def testWriteNonEscapedSolidus(self):
        s = cjson.encode(r'/')
        self.assertEqual(r'"/"', _removeWhitespace(s))

    def testWriteEscapedReverseSolidus(self):
        s = cjson.encode("\\")
        self.assertEqual(r'"\\"', _removeWhitespace(s))

    def testWriteEscapedBackspace(self):
        s = cjson.encode("\b")
        self.assertEqual(r'"\b"', _removeWhitespace(s))

    def testWriteEscapedFormfeed(self):
        s = cjson.encode("\f")
        self.assertEqual(r'"\f"', _removeWhitespace(s))

    def testWriteEscapedNewline(self):
        s = cjson.encode("\n")
        self.assertEqual(r'"\n"', _removeWhitespace(s))

    def testWriteEscapedCarriageReturn(self):
        s = cjson.encode("\r")
        self.assertEqual(r'"\r"', _removeWhitespace(s))

    def testWriteEscapedHorizontalTab(self):
        s = cjson.encode("\t")
        self.assertEqual(r'"\t"', _removeWhitespace(s))

    def testWriteEscapedHexCharacter(self):
        s = cjson.encode(u'\u1001')
        self.assertEqual(r'"\u1001"', _removeWhitespace(s))

    def testReadBadEscapedHexCharacter(self):
        self.assertRaises(_exception, self.doReadBadEscapedHexCharacter)

    def doReadBadEscapedHexCharacter(self):
        cjson.decode('"\u10K5"')

    def testReadBadObjectKey(self):
        self.assertRaises(_exception, self.doReadBadObjectKey)

    def doReadBadObjectKey(self):
        cjson.decode('{ 44 : "age" }')

    def testReadBadArray(self):
        self.assertRaises(_exception, self.doReadBadArray)

    def doReadBadArray(self):
        cjson.decode('[1,2,3,,]')
        
    def testReadBadObjectSyntax(self):
        self.assertRaises(_exception, self.doReadBadObjectSyntax)

    def doReadBadObjectSyntax(self):
        cjson.decode('{"age", 44}')

    def testWriteStringValue(self):
        s = cjson.encode({ "name" : "Patrick" })
        self.assertEqual('{"name":"Patrick"}', _removeWhitespace(s))

    def testReadIntegerValue(self):
        obj = cjson.decode('{ "age" : 44 }')
        self.assertEqual({ "age" : 44 }, obj)

    def testReadNegativeIntegerValue(self):
        obj = cjson.decode('{ "key" : -44 }')
        self.assertEqual({ "key" : -44 }, obj)
        
    def testReadFloatValue(self):
        obj = cjson.decode('{ "age" : 44.5 }')
        self.assertEqual({ "age" : 44.5 }, obj)

    def testReadNegativeFloatValue(self):
        obj = cjson.decode(' { "key" : -44.5 } ')
        self.assertEqual({ "key" : -44.5 }, obj)

    def testReadBadNumber(self):
        self.assertRaises(_exception, self.doReadBadNumber)

    def doReadBadNumber(self):
        cjson.decode('-44.4.4')

    def testReadSmallObject(self):
        obj = cjson.decode('{ "name" : "Patrick", "age":44} ')
        self.assertEqual({ "age" : 44, "name" : "Patrick" }, obj)        

    def testReadEmptyArray(self):
        obj = cjson.decode('[]')
        self.assertEqual([], obj)

    def testWriteEmptyArray(self):
        self.assertEqual("[]", _removeWhitespace(cjson.encode([])))

    def testReadSmallArray(self):
        obj = cjson.decode(' [ "a" , "b", "c" ] ')
        self.assertEqual(["a", "b", "c"], obj)

    def testWriteSmallArray(self):
        self.assertEqual('[1,2,3,4]', _removeWhitespace(cjson.encode([1, 2, 3, 4])))

    def testWriteSmallObject(self):
        s = cjson.encode({ "name" : "Patrick", "age": 44 })
        self.assertEqual('{"age":44,"name":"Patrick"}', _removeWhitespace(s))

    def testWriteFloat(self):
        self.assertEqual("3.44556677", _removeWhitespace(cjson.encode(3.44556677)))

    def testReadTrue(self):
        self.assertEqual(True, cjson.decode("true"))

    def testReadFalse(self):
        self.assertEqual(False, cjson.decode("false"))

    def testReadNull(self):
        self.assertEqual(None, cjson.decode("null"))

    def testWriteTrue(self):
        self.assertEqual("true", _removeWhitespace(cjson.encode(True)))

    def testWriteFalse(self):
        self.assertEqual("false", _removeWhitespace(cjson.encode(False)))

    def testWriteNull(self):
        self.assertEqual("null", _removeWhitespace(cjson.encode(None)))

    def testReadArrayOfSymbols(self):
        self.assertEqual([True, False, None], cjson.decode(" [ true, false,null] "))

    def testWriteArrayOfSymbolsFromList(self):
        self.assertEqual("[true,false,null]", _removeWhitespace(cjson.encode([True, False, None])))

    def testWriteArrayOfSymbolsFromTuple(self):
        self.assertEqual("[true,false,null]", _removeWhitespace(cjson.encode((True, False, None))))

    def testReadComplexObject(self):
        src = '''
    { "name": "Patrick", "age" : 44, "Employed?" : true, "Female?" : false, "grandchildren":null }
'''
        obj = cjson.decode(src)
        self.assertEqual({"name":"Patrick","age":44,"Employed?":True,"Female?":False,"grandchildren":None}, obj)

    def testReadLongArray(self):
        src = '''[    "used",
    "abused",
    "confused",
    true, false, null,
    1,
    2,
    [3, 4, 5]]
'''
        obj = cjson.decode(src)
        self.assertEqual(["used","abused","confused", True, False, None,
                          1,2,[3,4,5]], obj)

    def testReadIncompleteArray(self):
        self.assertRaises(_exception, self.doReadIncompleteArray)

    def doReadIncompleteArray(self):
        cjson.decode('[')

    def testReadComplexArray(self):
        src = '''
[
    { "name": "Patrick", "age" : 44,
      "Employed?" : true, "Female?" : false,
      "grandchildren":null },
    "used",
    "abused",
    "confused",
    1,
    2,
    [3, 4, 5]
]
'''
        obj = cjson.decode(src)
        self.assertEqual([{"name":"Patrick","age":44,"Employed?":True,"Female?":False,"grandchildren":None},
                          "used","abused","confused",
                          1,2,[3,4,5]], obj)

    def testWriteComplexArray(self):
        obj = [{"name":"Patrick","age":44,"Employed?":True,"Female?":False,"grandchildren":None},
               "used","abused","confused",
               1,2,[3,4,5]]
        self.assertEqual('[{"Female?":false,"age":44,"name":"Patrick","grandchildren":null,"Employed?":true},"used","abused","confused",1,2,[3,4,5]]',
                         _removeWhitespace(cjson.encode(obj)))


    def testReadWriteCopies(self):
        orig_obj = {'a':' " '}
        json_str = cjson.encode(orig_obj)
        copy_obj = cjson.decode(json_str)
        self.assertEqual(orig_obj, copy_obj)
        self.assertEqual(True, orig_obj == copy_obj)
        self.assertEqual(False, orig_obj is copy_obj)

    def testStringEncoding(self):
        s = cjson.encode([1, 2, 3])
        self.assertEqual(unicode("[1,2,3]", "utf-8"), _removeWhitespace(s))

    def testReadEmptyObjectAtEndOfArray(self):
        self.assertEqual(["a","b","c",{}],
                         cjson.decode('["a","b","c",{}]'))

    def testReadEmptyObjectMidArray(self):
        self.assertEqual(["a","b",{},"c"],
                         cjson.decode('["a","b",{},"c"]'))

    def testReadClosingObjectBracket(self):
        self.assertEqual({"a":[1,2,3]}, cjson.decode('{"a":[1,2,3]}'))

    def testEmptyObjectInList(self):
        obj = cjson.decode('[{}]')
        self.assertEqual([{}], obj)

    def testObjectWithEmptyList(self):
        obj = cjson.decode('{"test": [] }')
        self.assertEqual({"test":[]}, obj)

    def testObjectWithNonEmptyList(self):
        obj = cjson.decode('{"test": [3, 4, 5] }')
        self.assertEqual({"test":[3, 4, 5]}, obj)

    def testWriteLong(self):
        self.assertEqual("12345678901234567890", cjson.encode(12345678901234567890))
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
