#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bracex
Version  : 2.2.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/bd/ef/6273bba9e5bc615aab4997159eeaddfe03c825eeabe2942c39e91be5afec/bracex-2.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/ef/6273bba9e5bc615aab4997159eeaddfe03c825eeabe2942c39e91be5afec/bracex-2.2.1.tar.gz
Summary  : Bash style brace expander.
Group    : Development/Tools
License  : MIT
Requires: pypi-bracex-license = %{version}-%{release}
Requires: pypi-bracex-python = %{version}-%{release}
Requires: pypi-bracex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
[![Donate via PayPal][donate-image]][donate-link]
[![Discord][discord-image]][discord-link]
[![Build][github-ci-image]][github-ci-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]
[![PyPI - Python Version][python-image]][pypi-link]
![License][license-image-mit]
# Bracex

%package license
Summary: license components for the pypi-bracex package.
Group: Default

%description license
license components for the pypi-bracex package.


%package python
Summary: python components for the pypi-bracex package.
Group: Default
Requires: pypi-bracex-python3 = %{version}-%{release}

%description python
python components for the pypi-bracex package.


%package python3
Summary: python3 components for the pypi-bracex package.
Group: Default
Requires: python3-core
Provides: pypi(bracex)

%description python3
python3 components for the pypi-bracex package.


%prep
%setup -q -n bracex-2.2.1
cd %{_builddir}/bracex-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649721888
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bracex
cp %{_builddir}/bracex-2.2.1/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-bracex/64b6788556415e2e23a472f9de4eba6bfc9f1847
cp %{_builddir}/bracex-2.2.1/docs/src/markdown/about/license.md %{buildroot}/usr/share/package-licenses/pypi-bracex/92e0ed1c5183910686b14c1fd37184cd086409e8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bracex/64b6788556415e2e23a472f9de4eba6bfc9f1847
/usr/share/package-licenses/pypi-bracex/92e0ed1c5183910686b14c1fd37184cd086409e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
