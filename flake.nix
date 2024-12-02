{
  description = "Python application flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    deps = with pkgs; [aoc-cli (python3.withPackages pyDeps)];
    pyDeps = p: with p; [numpy];
  in {
    devShells.${system}.default = pkgs.mkShell {buildInputs = deps;};
  };
}
