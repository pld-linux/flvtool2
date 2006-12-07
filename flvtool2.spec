%define		_rc	rc6
Summary:	Manipulation tool for Macromedia Flash Video files
Name:		flvtool2
Version:	1.0.5
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://rubyforge.org/frs/download.php/9225/%{name}_%{version}_%{_rc}.tgz
# Source0-md5:	6cf448db50936251992b4812b6381f69
URL:		http://rubyforge.org/projects/flvtool2/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLVTool2 is a manipulation tool for Macromedia Flash Video files
(FLV). It can calculate a lot of meta data, insert an onMetaData tag,
cut FLV files, add cue points (onCuePoint), show the FLV structure and
print meta data information in XML or YAML.

%prep
%setup -q -n %{name}_%{version}_%{_rc}

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

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