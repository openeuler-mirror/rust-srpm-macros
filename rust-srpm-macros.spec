Name:           rust-srpm-macros
Version:        21
Release:        1
Summary:        RPM macros for building Rust source packages

License:        MIT
URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         https://pagure.io/fedora-rust/rust2rpm/archive/v%{version}/rust2rpm-v%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n rust2rpm-v%{version} -p1
# https://pagure.io/koji/issue/659
sed -i -e 's/i686/%%{ix86}/' data/macros.rust-srpm

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.rust-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm

%changelog
* Sat May 07 2022 jchzhou <jchzhou@outlook.com> - 21-1
- Init package from fedora
- Upstream: https://src.fedoraproject.org/rpms/rust-srpm-macros maintained by Igor Raits