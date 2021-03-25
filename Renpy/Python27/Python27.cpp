#include "Python.h"

#include <ppltasks.h>
#include <inspectable.h>
#include <wrl.h>
#include <robuffer.h>
#include <windows.storage.streams.h>

using namespace Windows::Storage;
using namespace Windows::Storage::Streams;
using namespace Windows::Security::Cryptography;
using namespace Microsoft::WRL;
using namespace Platform;
using namespace Concurrency;

extern "C" {

    void win32_urandom(unsigned char* buffer, Py_ssize_t size, int raise)
    {
        IBuffer^ data = CryptographicBuffer::GenerateRandom(size);
        Array<unsigned char>^ data2;
        CryptographicBuffer::CopyToByteArray(data, &data2);
        for (int i = 0; i < size; i++)
            buffer[i] = data2[i];
    }

}