# $Revision: 1.39 $Date: 2002-02-22 23:29:20 $
#
# Conditional builds:	
# --with openldap1 - build with openldap < 2.0.0
#
Summary:	LDAP Name Service Switch Module
Summary(pl):	Modu³ NSS LDAP
Name:		nss_ldap
Version:	173
Release:	3
License:	LGPL
Group:		Base
Source0:	ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_with_openldap1:BuildRequires: openldap-devel >= 2.0.0}
%{?_with_openldap1:BuildRequires:  openldap-devel <  2.0.0}
%{?_with_openldap1:BuildRequires:  openldap-devel >  1.2.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib

%description 
This is nss_ldap, a name service switch module that can be used with
glibc-2.1.xx.

%description -l pl
To jest nss_ldap - modu³ serwisu nazw odczytuj±cy dane z LDAP, który
mo¿na u¿ywaæ z glibc.

%prep
%setup -q
%patch -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--with-ldap-lib=openldap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE AUTHORS ChangeLog NEWS README nsswitch* doc/rfc*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(0755,root,root) %{_libdir}/*.so*
