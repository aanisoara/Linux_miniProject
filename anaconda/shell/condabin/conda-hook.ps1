$Env:CONDA_EXE = "/root/projet_linux/anacondaa/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/root/projet_linux/anacondaa"
$Env:_CONDA_EXE = "/root/projet_linux/anacondaa/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $True}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs