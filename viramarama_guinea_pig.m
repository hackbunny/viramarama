// viramarama_guinea_pig -- trivial test program for CoreText, suitable as a
// fuzzing driver.
//
// How to build (all on one line):
//
// $ clang -framework Foundation -framework Cocoa -O3 -o viramarama_guinea_pig
//       viramarama_guinea_pig.m
//
// Usage:
//
// $ viramarama_guinea_pig STRING
//
// The program will try to render STRING using the CoreText framework, returning
// success (0) if rendering completed successfully or failure (1) if a crash
// occurred. For more reliable results, run with Guard Malloc, e.g.:
//
// $ DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib viramarama_guinea_pig STRING
//
// Copyright 2018 hackbunny <hackbunny@gmail.com>
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#include <signal.h>
#include <stdlib.h>

#import <Foundation/Foundation.h>
#import <Cocoa/Cocoa.h>

static void crash_handler(int signo) {
    _exit(EXIT_FAILURE);
}

int main(int argc, const char *argv[]) {
    if (argc < 2)
        return 255;
    
    signal(SIGSEGV, crash_handler);
    signal(SIGABRT, crash_handler);
    
    @autoreleasepool {
        [NSTextField textFieldWithString:[NSString stringWithUTF8String:argv[1]]];
    }
    
    return 0;
}
