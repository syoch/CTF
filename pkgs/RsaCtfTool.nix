{ buildPythonPackage, fetchFromGitHub }:
(buildPythonPackage {
  pname = "RsaCtfTool";
  version = "1.0.0";
  format = "setuptools";
  src = fetchFromGitHub {
    owner = "RsaCtfTool";
    repo = "RsaCtfTool";
    rev = "master";
    sha256 = "sha256-xttrOyStaTy6ZoL+2S3oVbEidiq0hukKDZsN0WM4Zdw=";
  };
})
