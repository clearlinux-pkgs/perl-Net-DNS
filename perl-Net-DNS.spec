#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-DNS
Version  : 1.25
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-1.25.tar.gz
Summary  : 'Perl Interface to the Domain Name System'
Group    : Development/Tools
License  : MIT
Requires: perl-Net-DNS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::HMAC)

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


%package perl
Summary: perl components for the perl-Net-DNS package.
Group: Default
Requires: perl-Net-DNS = %{version}-%{release}

%description perl
perl components for the perl-Net-DNS package.


%prep
%setup -q -n Net-DNS-1.25
cd %{_builddir}/Net-DNS-1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Domain.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/DomainName.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/FAQ.pod
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Header.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Mailbox.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Nameserver.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Packet.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Parameters.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Question.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/A.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/AAAA.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/AFSDB.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/AMTRELAY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/APL.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CAA.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CDNSKEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CDS.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CERT.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CNAME.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/CSYNC.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/DHCID.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/DNAME.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/DNSKEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/DS.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/EUI48.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/EUI64.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/GPOS.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/HINFO.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/HIP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/IPSECKEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/ISDN.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/KEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/KX.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/L32.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/L64.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/LOC.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/LP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/MB.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/MG.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/MINFO.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/MR.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/MX.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NAPTR.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NID.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NS.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NSEC.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NSEC3.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NSEC3PARAM.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/NULL.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/OPENPGPKEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/OPT.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/PTR.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/PX.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/RP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/RRSIG.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/RT.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SIG.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SMIMEA.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SOA.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SPF.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SRV.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/SSHFP.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/TKEY.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/TLSA.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/TSIG.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/TXT.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/URI.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/X25.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/RR/ZONEMD.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/Base.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/MSWin32.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/Recurse.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/UNIX.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/android.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/cygwin.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/os2.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Resolver/os390.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Text.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/Update.pm
/usr/lib/perl5/vendor_perl/5.30.3/Net/DNS/ZoneFile.pm
