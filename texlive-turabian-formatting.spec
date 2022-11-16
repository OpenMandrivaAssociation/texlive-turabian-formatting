Name:		texlive-turabian-formatting
Version:	58561
Release:	1
Summary:	Formatting based on Turabian's Manual
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/turabian-formatting
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian-formatting.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian-formatting.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The turabian-formatting package provides Chicago-style
formatting based on Kate L. Turabian's "A Manual for Writers of
Research Papers, Theses, and Dissertations: Chicago Style for
Students and Researchers" (9th edition).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/turabian-formatting
%doc %{_texmfdistdir}/doc/latex/turabian-formatting

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
