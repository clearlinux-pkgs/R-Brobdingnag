#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Brobdingnag
Version  : 1.2.6
Release  : 31
URL      : https://cran.r-project.org/src/contrib/Brobdingnag_1.2-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Brobdingnag_1.2-6.tar.gz
Summary  : Very Large Numbers in R
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
using their natural logarithms, plus a logical flag indicating
        sign.  The package includes a vignette that gives a
        step-by-step introduction to using S4 methods.

%prep
%setup -q -c -n Brobdingnag
cd %{_builddir}/Brobdingnag

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589516042

%install
export SOURCE_DATE_EPOCH=1589516042
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Brobdingnag
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Brobdingnag
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Brobdingnag
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Brobdingnag || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Brobdingnag/CITATION
/usr/lib64/R/library/Brobdingnag/DESCRIPTION
/usr/lib64/R/library/Brobdingnag/INDEX
/usr/lib64/R/library/Brobdingnag/Meta/Rd.rds
/usr/lib64/R/library/Brobdingnag/Meta/features.rds
/usr/lib64/R/library/Brobdingnag/Meta/hsearch.rds
/usr/lib64/R/library/Brobdingnag/Meta/links.rds
/usr/lib64/R/library/Brobdingnag/Meta/nsInfo.rds
/usr/lib64/R/library/Brobdingnag/Meta/package.rds
/usr/lib64/R/library/Brobdingnag/Meta/vignette.rds
/usr/lib64/R/library/Brobdingnag/NAMESPACE
/usr/lib64/R/library/Brobdingnag/R/Brobdingnag
/usr/lib64/R/library/Brobdingnag/R/Brobdingnag.rdb
/usr/lib64/R/library/Brobdingnag/R/Brobdingnag.rdx
/usr/lib64/R/library/Brobdingnag/doc/S4_brob.R
/usr/lib64/R/library/Brobdingnag/doc/S4_brob.Rnw
/usr/lib64/R/library/Brobdingnag/doc/S4_brob.pdf
/usr/lib64/R/library/Brobdingnag/doc/brobpaper.R
/usr/lib64/R/library/Brobdingnag/doc/brobpaper.Rnw
/usr/lib64/R/library/Brobdingnag/doc/brobpaper.pdf
/usr/lib64/R/library/Brobdingnag/doc/index.html
/usr/lib64/R/library/Brobdingnag/help/AnIndex
/usr/lib64/R/library/Brobdingnag/help/Brobdingnag.rdb
/usr/lib64/R/library/Brobdingnag/help/Brobdingnag.rdx
/usr/lib64/R/library/Brobdingnag/help/aliases.rds
/usr/lib64/R/library/Brobdingnag/help/paths.rds
/usr/lib64/R/library/Brobdingnag/html/00Index.html
/usr/lib64/R/library/Brobdingnag/html/R.css
