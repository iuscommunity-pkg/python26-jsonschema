%define __python /usr/bin/python2.6
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define py_basever 26
%define real_name python-jsonschema
%define name python%{py_basever}-jsonschema

Name:           %{name} 
Version:        0.2a
Release:        1.ius%{?dist}
Summary:        JSON Schema is a specification for defining the structure of JSON data. 

Group:          System Environment/Libraries
License:        MIT
URL:            http://code.google.com/p/jsonschema/ 
Source0:        http://jsonschema.googlecode.com/files/jsonschema-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  python%{py_basever}-devel
BuildRequires:  python%{py_basever}-setuptools
Requires:       python%{py_basever}

%description
JSON Schema is a specification for a JSON-based format for defining 
the structure of JSON data. JSON Schema provides a contract for what 
JSON data is required for a given application and how it can be 
modified, much like what XML Schema provides for XML. JSON Schema is 
intended to provide validation, documentation, and interaction control 
of JSON data.


%prep
%setup -q -n jsonschema-%{version}


%build
%{__python} setup.py build


%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot} \
                                 --single-version-externally-managed


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs examples LICENSE.txt README.txt README.ja.utf8.txt
%{python_sitelib}/jsonschema
%{python_sitelib}/jsonschema-%{version}-py%{pyver}.egg-info


%changelog
* Thu Feb 03 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> 0.2a-2.ius
- Removed sitearch and replaced with sitelib as this is a noarch package

* Mon Aug 25 2009 BJ Dierkes <wdierkes@rackspace.com> 0.2a-1.ius
- Initial spec build
