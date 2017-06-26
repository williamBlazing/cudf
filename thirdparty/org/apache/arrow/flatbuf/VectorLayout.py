# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers

# /// ----------------------------------------------------------------------
# /// represents the physical layout of a buffer
# /// buffers have fixed width slots of a given type
class VectorLayout(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVectorLayout(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VectorLayout()
        x.Init(buf, n + offset)
        return x

    # VectorLayout
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// the width of a slot in the buffer (typically 1, 8, 16, 32 or 64)
    # VectorLayout
    def BitWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

# /// the purpose of the vector
    # VectorLayout
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def VectorLayoutStart(builder): builder.StartObject(2)
def VectorLayoutAddBitWidth(builder, bitWidth): builder.PrependInt16Slot(0, bitWidth, 0)
def VectorLayoutAddType(builder, type): builder.PrependInt16Slot(1, type, 0)
def VectorLayoutEnd(builder): return builder.EndObject()