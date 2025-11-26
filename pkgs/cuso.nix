{
  buildPythonPackage,
  fetchFromGitHub, 
  fpylll,
  igraph,
  setuptools,

  singular,

  sage
}:
(buildPythonPackage {
  pname = "cuso";
  version = "1.0.0";
  pyproject = true;
  build-system = [
    setuptools
  ];

  buildInputs = [ singular ];

  dependencies = [
    fpylll
    igraph
    sage
  ];

  src = fetchFromGitHub {
    owner = "keeganryan";
    repo = "cuso";
    rev = "master";
    sha256 = "sha256-RYzTuu1h9bedsDBYr3j8eU253ks/7IahvIYQk0tVCCc=";
  };
})
