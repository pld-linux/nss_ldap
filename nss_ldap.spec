Summary:	LDAP Name Service Switch Module
Summary(es.UTF-8):	Biblioteca NSS para LDAP
Summary(pl.UTF-8):	Moduł NSS LDAP
Summary(pt_BR.UTF-8):	Biblioteca NSS para LDAP
Name:		nss_ldap
Version:	265
Release:	1
License:	LGPL
Group:		Base
Source0:	http://www.padl.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	c1cb02d1a85538cf16bca6f6a562abe4
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-gecos-optional.patch
Patch3:		%{name}-group_range_fix.patch
Patch4:		%{name}-soname.patch
Patch5:		%{name}-heimdal.patch
URL:		http://www.padl.com/OSS/nss_ldap.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	cyrus-sasl-devel
Requires:	openldap-nss-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
nss_ldap is a C library extension (NSS module) which allows X.500 and
LDAP directory servers to be used as a primary source of aliases,
ethers, groups, hosts, networks, protocols, users, RPCs, services and
shadow passwords (instead of or in addition to using flat files or
NIS).

%description -l es.UTF-8
Este paquete contiene dos clientes de acceso a LDAP: nss_ldap y
pam_ldap.

nss_ldap son una serie de extensiones para la biblioteca C que
permiten que directorios X.500 y LDAP se usen como fuente de alias,
grupos, máquinas, protocolos, usuarios, RPCs, etc. (en vez de, o en
añadidura a, archivos normales o NIS)

pam_ldap es un módulo para Linux-PAM que da soporte al intercambio de
señas, clientes V2, Netscape SSL, ypldapd, políticas de contraseñas
Netscape Directory Server, autorización de acceso, hashes codificados,
etc.

%description -l pl.UTF-8
To jest nss_ldap - moduł serwisu nazw odczytujący dane z LDAP, który
można używać z glibc. Pozwala na korzystanie z serwerów X.500 i LDAP
jako głównego źródła aliasów, grup, hostów, sieci, protokołów,
użytkowników, RPC, usług i haseł (zamiast lub oprócz zwykłych plików
lub NIS).

%description -l pt_BR.UTF-8
Esse pacote contém dois clientes de acesso a LDAP: nss_ldap e
pam_ldap.

nss_ldap é uma série de extensões para a biblioteca C que permitem que
diretórios X.500 e LDAP sejam usados como fonte de apelidos, grupos,
máquinas, protocolos, usuários, RPCs, etc. (ao invés de, ou em adição
a, arquivos normais ou NIS)

pam_ldap é um módulo para o Linux-PAM que dá suporte a troca de
senhas, clientes V2, Netscape SSL, ypldapd, políticas de senhas
Netscape Directory Server, autorização de acesso, hashes encriptados,
etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e "s#NSS_VERS =.*#NSS_VERS = $(ls /%{_lib}/libnss_files.so.? | tail -n 1 | sed -e 's#/%{_lib}/libnss_files\.so\.\(.*\)#\1#')#g" Makefile.am
sed -i -e "s#LIBC_VERS =.*#LIBC_VERS = $(ls /%{_lib}/libc-*.so | tail -n 1 |sed -e 's#/%{_lib}/libc-\(.*\)\.so#\1#')#g" Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -DHEIMDAL" ; export CFLAGS
%configure \
	--with-ldap-lib=openldap \
	--enable-rfc2307bis \
	--enable-paged-results \
	--enable-configurable-krb5-ccname-env \
	--enable-configurable-krb5-ccname-gssapi \
	--enable-configurable-krb5-keytab

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog NEWS README nsswitch* ldap.conf
%attr(755,root,root) %{_libdir}/*.so*
%{_mandir}/man5/*
