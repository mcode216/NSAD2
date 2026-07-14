import ROOT


inputfile1 = ROOT.TFile("ukolwrad.root", "READ")
inputfile2 = ROOT.TFile("ukolnrad.root", "READ")

pt1 = inputfile1.Get("h_pT")
pt2 = inputfile2.Get("h_pT")

y1 = inputfile1.Get("h_rap")
y2 = inputfile2.Get("h_rap")


pt1.SetLineColor(ROOT.kRed)
pt2.SetLineColor(ROOT.kBlue)

y1.SetLineColor(ROOT.kRed)
y2.SetLineColor(ROOT.kBlue)

y1.SetStats(0)
y2.SetStats(0)

can1 = ROOT.TCanvas("can1", "", 1200, 500)
maxY = max(pt1.GetMaximum(), pt2.GetMaximum())
pt1.SetMaximum(maxY * 1.1)
pt1.Draw()
pt2.Draw("SAME")
legend = ROOT.TLegend(0.6, 0.7, 0.88, 0.88)  
legend.SetBorderSize(0)
legend.SetTextSize(0.03)
legend.AddEntry(pt1, "rad on", "l")  
legend.AddEntry(pt2, "rad off", "l")
legend.Draw()


can2 = ROOT.TCanvas("can2", "", 1200, 500)
maxY = max(y1.GetMaximum(), y2.GetMaximum())
y1.SetMaximum(maxY * 1.1)
y1.Draw()
y2.Draw("SAME")
legend2 = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend2.SetBorderSize(0)
legend2.SetTextSize(0.03)
legend2.AddEntry(y1, "rad on", "l")
legend2.AddEntry(y2, "rad off", "l")
legend2.Draw()

can1.SaveAs("pt.pdf")
can2.SaveAs("y.pdf")