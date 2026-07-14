import pythia8
import ROOT

root_file = ROOT.TFile("ukolnrad.root", "RECREATE")
pythia = pythia8.Pythia()

pythia.readString("Beams:idA = 2212")
pythia.readString("Beams:idB = 2212")
pythia.readString("Beams:eCM = 13000")
pythia.readString("HiggsSM:all = on")
pythia.readString("PartonLevel:ISR = off")

pythia.init()

h_pT = ROOT.TH1D("h_pT", "Higgs boson p_{T} spectrum;p_{T} [GeV/c];Events", 100,0.0,100.0)
h_rap = ROOT.TH1D("h_rap", "Higgs boson rapidity y;y [-];Events", 100,-3,3)

for i in range(20000):
    if not pythia.next():
        continue
    for p in pythia.event:
        if p.id() == 25 and p.daughter2()>p.daughter1():
            h_pT.Fill(p.pT())
            h_rap.Fill(p.y())
            break

h_pT.Write()
h_rap.Write()
root_file.Close()
