class Vce < Formula
  desc "Randroid's Text to Voice Script. Using OpenAI's API."
  homepage "https://github.com/randroid88/homebrew-vce"
  url "https://github.com/randroid88/homebrew-vce/archive/refs/tags/1.0.1.tar.gz"
  sha256 "dc12c909b9726dbfac883911a6d045ac75c0fa470541c3f3220db9862efab61d"

  # uses_from_macos "python@3"

  def install
    libexec.install Dir["*.py"]

    # Write a wrapper script and install it to bin
    (bin/"vce").write <<~EOS
      #!/bin/bash
      /usr/bin/env python3 "#{libexec}/vce.py" "$@"
    EOS
  end

  test do
    system "#{bin}/vce"
  end
end