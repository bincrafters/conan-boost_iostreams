#include <boost/iostreams/filtering_stream.hpp>

#ifdef WITH_ZLIB
  #include <boost/iostreams/filter/zlib.hpp>
  #include <boost/iostreams/filter/gzip.hpp>
#endif
#ifdef WITH_BZIP2
  #include <boost/iostreams/filter/bzip2.hpp>
#endif
#ifdef WITH_LZMA
  #include <boost/iostreams/filter/lzma.hpp>
#endif

int main()
{
    boost::iostreams::filtering_ostream os;

#ifdef WITH_ZLIB
    boost::iostreams::zlib_compressor();
    boost::iostreams::gzip_compressor();
#endif
#ifndef WITH_BZIP2
    boost::iostreams::bzip2_compressor();
#endif
#ifdef WITH_LZMA
    boost::iostreams::lzma_compressor();
#endif
}
