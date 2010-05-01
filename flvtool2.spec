Summary:	Manipulation tool for Macromedia Flash Video files
Summary(pl.UTF-8):	Narzędzie do obróbki plików Macromedia Flash Video
Name:		flvtool2
Version:	1.0.6
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://rubyforge.org/frs/download.php/17497/%{name}-%{version}.tgz
# Source0-md5:	08e5f6f10c06903447d97d7ba10cec67
URL:		http://rubyforge.org/projects/flvtool2/
Patch0:		%{name}-ruby19.patch
BuildRequires:	rpmbuild(macros) >= 1.279
BuildRequires:	ruby
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLVTool2 is a manipulation tool for Macromedia Flash Video files
(FLV). It can calculate a lot of meta data, insert an onMetaData tag,
cut FLV files, add cue points (onCuePoint), show the FLV structure and
print meta data information in XML or YAML.

%description -l pl.UTF-8
FLVTool2 to narzędzie do obróbki plików Macromedia Flash Video (FLV).
Potrafi obliczać większość metadanych, wstawiać znaczniki onMetaData,
ciąć pliki FLV, dodawać punkty wskazań (onCuePoint), pokazywać
strukturę FLV i wypisywać informacje o metadanych w formacie XML lub
YAML.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README
%attr(755,root,root) %{_bindir}/flvtool2
%{ruby_rubylibdir}/flv.rb
%dir %{ruby_rubylibdir}/flv
%{ruby_rubylibdir}/flv/amf_string_buffer.rb
%{ruby_rubylibdir}/flv/audio_tag.rb
%{ruby_rubylibdir}/flv/core_extensions.rb
%{ruby_rubylibdir}/flv/meta_tag.rb
%{ruby_rubylibdir}/flv/stream.rb
%{ruby_rubylibdir}/flv/tag.rb
%{ruby_rubylibdir}/flv/video_tag.rb
%{ruby_rubylibdir}/flvtool2.rb
%dir %{ruby_rubylibdir}/flvtool2
%{ruby_rubylibdir}/flvtool2/base.rb
%{ruby_rubylibdir}/flvtool2/version.rb
%{ruby_rubylibdir}/mixml.rb
%{ruby_rubylibdir}/miyaml.rb
%{_examplesdir}/%{name}-%{version}
