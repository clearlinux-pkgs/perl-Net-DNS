#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Net-DNS
Version  : 1.38
Release  : 47
URL      : https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-1.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-1.38.tar.gz
Summary  : 'Perl Interface to the Domain Name System'
Group    : Development/Tools
License  : HPND MIT
Requires: perl-Net-DNS-license = %{version}-%{release}
Requires: perl-Net-DNS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::HMAC)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Net::DNS - Perl DNS Resolver Module
===================================
TABLE OF CONTENTS
-----------------

%package dev
Summary: dev components for the perl-Net-DNS package.
Group: Development
Provides: perl-Net-DNS-devel = %{version}-%{release}
Requires: perl-Net-DNS = %{version}-%{release}

%description dev
dev components for the perl-Net-DNS package.


%package license
Summary: license components for the perl-Net-DNS package.
Group: Default

%description license
license components for the perl-Net-DNS package.


%package perl
Summary: perl components for the perl-Net-DNS package.
Group: Default
Requires: perl-Net-DNS = %{version}-%{release}

%description perl
perl components for the perl-Net-DNS package.


%prep
%setup -q -n Net-DNS-1.38
cd %{_builddir}/Net-DNS-1.38
pushd ..
cp -a Net-DNS-1.38 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-DNS
cp %{_builddir}/Net-DNS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-DNS/9f8614708dc64fcecc6498bda205c238eeced92f || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::DNS.3
/usr/share/man/man3/Net::DNS::Domain.3
/usr/share/man/man3/Net::DNS::DomainName.3
/usr/share/man/man3/Net::DNS::FAQ.3
/usr/share/man/man3/Net::DNS::Header.3
/usr/share/man/man3/Net::DNS::Mailbox.3
/usr/share/man/man3/Net::DNS::Nameserver.3
/usr/share/man/man3/Net::DNS::Packet.3
/usr/share/man/man3/Net::DNS::Parameters.3
/usr/share/man/man3/Net::DNS::Question.3
/usr/share/man/man3/Net::DNS::RR.3
/usr/share/man/man3/Net::DNS::RR::A.3
/usr/share/man/man3/Net::DNS::RR::AAAA.3
/usr/share/man/man3/Net::DNS::RR::AFSDB.3
/usr/share/man/man3/Net::DNS::RR::AMTRELAY.3
/usr/share/man/man3/Net::DNS::RR::APL.3
/usr/share/man/man3/Net::DNS::RR::CAA.3
/usr/share/man/man3/Net::DNS::RR::CDNSKEY.3
/usr/share/man/man3/Net::DNS::RR::CDS.3
/usr/share/man/man3/Net::DNS::RR::CERT.3
/usr/share/man/man3/Net::DNS::RR::CNAME.3
/usr/share/man/man3/Net::DNS::RR::CSYNC.3
/usr/share/man/man3/Net::DNS::RR::DHCID.3
/usr/share/man/man3/Net::DNS::RR::DNAME.3
/usr/share/man/man3/Net::DNS::RR::DNSKEY.3
/usr/share/man/man3/Net::DNS::RR::DS.3
/usr/share/man/man3/Net::DNS::RR::EUI48.3
/usr/share/man/man3/Net::DNS::RR::EUI64.3
/usr/share/man/man3/Net::DNS::RR::GPOS.3
/usr/share/man/man3/Net::DNS::RR::HINFO.3
/usr/share/man/man3/Net::DNS::RR::HIP.3
/usr/share/man/man3/Net::DNS::RR::HTTPS.3
/usr/share/man/man3/Net::DNS::RR::IPSECKEY.3
/usr/share/man/man3/Net::DNS::RR::ISDN.3
/usr/share/man/man3/Net::DNS::RR::KEY.3
/usr/share/man/man3/Net::DNS::RR::KX.3
/usr/share/man/man3/Net::DNS::RR::L32.3
/usr/share/man/man3/Net::DNS::RR::L64.3
/usr/share/man/man3/Net::DNS::RR::LOC.3
/usr/share/man/man3/Net::DNS::RR::LP.3
/usr/share/man/man3/Net::DNS::RR::MB.3
/usr/share/man/man3/Net::DNS::RR::MG.3
/usr/share/man/man3/Net::DNS::RR::MINFO.3
/usr/share/man/man3/Net::DNS::RR::MR.3
/usr/share/man/man3/Net::DNS::RR::MX.3
/usr/share/man/man3/Net::DNS::RR::NAPTR.3
/usr/share/man/man3/Net::DNS::RR::NID.3
/usr/share/man/man3/Net::DNS::RR::NS.3
/usr/share/man/man3/Net::DNS::RR::NSEC.3
/usr/share/man/man3/Net::DNS::RR::NSEC3.3
/usr/share/man/man3/Net::DNS::RR::NSEC3PARAM.3
/usr/share/man/man3/Net::DNS::RR::NULL.3
/usr/share/man/man3/Net::DNS::RR::OPENPGPKEY.3
/usr/share/man/man3/Net::DNS::RR::OPT.3
/usr/share/man/man3/Net::DNS::RR::PTR.3
/usr/share/man/man3/Net::DNS::RR::PX.3
/usr/share/man/man3/Net::DNS::RR::RP.3
/usr/share/man/man3/Net::DNS::RR::RRSIG.3
/usr/share/man/man3/Net::DNS::RR::RT.3
/usr/share/man/man3/Net::DNS::RR::SIG.3
/usr/share/man/man3/Net::DNS::RR::SMIMEA.3
/usr/share/man/man3/Net::DNS::RR::SOA.3
/usr/share/man/man3/Net::DNS::RR::SPF.3
/usr/share/man/man3/Net::DNS::RR::SRV.3
/usr/share/man/man3/Net::DNS::RR::SSHFP.3
/usr/share/man/man3/Net::DNS::RR::SVCB.3
/usr/share/man/man3/Net::DNS::RR::TKEY.3
/usr/share/man/man3/Net::DNS::RR::TLSA.3
/usr/share/man/man3/Net::DNS::RR::TSIG.3
/usr/share/man/man3/Net::DNS::RR::TXT.3
/usr/share/man/man3/Net::DNS::RR::URI.3
/usr/share/man/man3/Net::DNS::RR::X25.3
/usr/share/man/man3/Net::DNS::RR::ZONEMD.3
/usr/share/man/man3/Net::DNS::Resolver.3
/usr/share/man/man3/Net::DNS::Resolver::Base.3
/usr/share/man/man3/Net::DNS::Resolver::MSWin32.3
/usr/share/man/man3/Net::DNS::Resolver::Recurse.3
/usr/share/man/man3/Net::DNS::Resolver::UNIX.3
/usr/share/man/man3/Net::DNS::Resolver::android.3
/usr/share/man/man3/Net::DNS::Resolver::cygwin.3
/usr/share/man/man3/Net::DNS::Resolver::os2.3
/usr/share/man/man3/Net::DNS::Resolver::os390.3
/usr/share/man/man3/Net::DNS::Text.3
/usr/share/man/man3/Net::DNS::Update.3
/usr/share/man/man3/Net::DNS::ZoneFile.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-DNS/9f8614708dc64fcecc6498bda205c238eeced92f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
