Name:		texlive-termcal
Version:	22514
Release:	1
Summary:	Print a class calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termcal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is intended to print a term calendar for use in
planning a class. It has a flexible mechanism for specifying
which days of the week are to be included and for inserting
text either regularly on the same day each week, or on selected
days, or for a series of consecutive days. It also has a
flexible mechanism for specifing class and nonclass days. Text
may be inserted into consecutive days so that it automatically
flows around nonclass days.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/termcal/termcal.sty
%doc %{_texmfdistdir}/doc/latex/termcal/Contents
%doc %{_texmfdistdir}/doc/latex/termcal/README
%doc %{_texmfdistdir}/doc/latex/termcal/termcal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/termcal/termcal.dtx
%doc %{_texmfdistdir}/source/latex/termcal/termcal.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
