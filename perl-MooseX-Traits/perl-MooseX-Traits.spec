Name:           perl-MooseX-Traits
Summary:        Automatically apply roles at object creation time
Version:        0.11
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/MooseX-Traits-%{version}.tar.gz
URL:            http://search.cpan.org/dist/MooseX-Traits
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Class::MOP) >= 0.84
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(ok)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

Requires:       perl(Class::MOP) >= 0.84
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(namespace::autoclean)
Requires:       perl(Sub::Exporter)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
MooseX::Traits allows one to arbitrarily add components to an object as
needed, w/o having to explicitly construct new classes: e.g.

    Foo->with_traits('Bar')->new(...);

%prep
%setup -q -n MooseX-Traits-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sat May 29 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- additional br on MooseX::Role::Parameterized
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.11)
- added a new req on perl(Moose) (version 0.84)

* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- specfile by Fedora::App::MaintainerTools 0.006
