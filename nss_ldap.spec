#
# Conditional builds:
%bcond_with openldap1 	# build with openldap < 2.0.0
%bcond_without mapping	# build without support for schema mapping/rfc2307bis
Summary:	LDAP Name Service Switch Module
Summary(es):	Biblioteca NSS para LDAP
Summary(pl):	Modu� NSS LDAP
Summary(pt_BR):	Biblioteca NSS para LDAP
Name:		nss_ldap
Version:	211
Release:	1
License:	LGPL
Group:		Base
Source0:	http://www.padl.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	34adcab5d46a436617ae686cc7c5e78f
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-nolibs.patch
URL:		http://www.padl.com/nss_ldap.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_mapping:BuildRequires:	db-devel}
%{!?with_openldap1:BuildRequires:	openldap-devel >= 2.0.0}
%{?with_openldap1:BuildRequires:	openldap-devel <  2.0.0}
%{?with_openldap1:BuildRequires:	openldap-devel >  1.2.0}
BuildRequires:	cyrus-sasl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib

%description
nss_ldap is a C library extension (NSS module) which allows X.500 and
LDAP directory servers to be used as a primary source of aliases,
ethers, groups, hosts, networks, protocols, users, RPCs, services and
shadow passwords (instead of or in addition to using flat files or
NIS).

%description -l es
Este paquete contiene dos clientes de acceso a LDAP: nss_ldap y
pam_ldap.

nss_ldap son una serie de extensiones para la biblioteca C que
permiten que directorios X.500 y LDAP se usen como fuente de alias,
grupos, m�quinas, protocolos, usuarios, RPCs, etc. (en vez de, o en
a�adidura a, archivos normales o NIS)

pam_ldap es un m�dulo para Linux-PAM que da soporte al intercambio de
se�as, clientes V2, Netscape SSL, ypldapd, pol�ticas de contrase�as
Netscape Directory Server, autorizaci�n de acceso, hashes codificados,
etc.

%description -l pl
To jest nss_ldap - modu� serwisu nazw odczytuj�cy dane z LDAP, kt�ry
mo�na u�ywa� z glibc. Pozwala na korzystanie z serwer�w X.500 i LDAP
jako g��wnego �r�d�a alias�w, grup, host�w, sieci, protoko��w,
u�ytkownik�w, RPC, us�ug i hase� (zamiast lub opr�cz zwyk�ych plik�w
lub NIS).

%description -l pt_BR
Esse pacote cont�m dois clientes de acesso a LDAP: nss_ldap e
pam_ldap.

nss_ldap � uma s�rie de extens�es para a biblioteca C que permitem que
diret�rios X.500 e LDAP sejam usados como fonte de apelidos, grupos,
m�quinas, protocolos, usu�rios, RPCs, etc. (ao inv�s de, ou em adi��o
a, arquivos normais ou NIS)

pam_ldap � um m�dulo para o Linux-PAM que d� suporte a troca de
senhas, clientes V2, Netscape SSL, ypldapd, pol�ticas de senhas
Netscape Directory Server, autoriza��o de acesso, hashes encriptados,
etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ldap-lib=openldap \
%if %{with mapping}
	--enable-schema-mapping \
	--enable-rfc2307bis \
%endif
	--enable-paged-results \
	--enable-configurable-krb5-ccname

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
%attr(0755,root,root) %{_libdir}/*.so*
