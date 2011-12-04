Name: hunspell-az
Summary: Azerbaijani hunspell dictionaries
%define upstreamid 20040827
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Group: Applications/Text
Source: ftp://ftp.gnu.org/gnu/aspell/dict/az/aspell6-az-0.02-0.tar.bz2
URL: http://borel.slu.edu/crubadan/apps.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch
BuildRequires: aspell, hunspell-devel

Requires: hunspell

%description
Azerbaijani hunspell dictionaries.

%prep
%setup -q -n aspell6-az-0.02-0

%build
export LANG=az_AZ.utf8
preunzip az.cwl
wordlist2hunspell az.wl az_AZ
for i in Copyright doc/Crawler.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20040827-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040827-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20040827-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040827-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Caolan McNamara <caolanm@redhat.com> - 0.20040827-1
- initial version
