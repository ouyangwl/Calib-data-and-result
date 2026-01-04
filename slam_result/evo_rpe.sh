#evo_traj tum 3mycalib_new/mycalib_traj.txt 3kalibr/kalibr_traj.txt --ref=3groundtruth.txt -asp --plot_mode=xy


evo_rpe tum 2groundtruth.txt 2mycalib/mycalib_traj.txt -r trans_part --delta 1 --delta_unit m -vasp --save_results paper_result/2rpe_mycalib.zip
evo_rpe tum 2groundtruth.txt 2kalibr/kalibr_traj.txt -r trans_part --delta 1 --delta_unit m -vasp --save_results paper_result/2rpe_kalibr.zip
evo_res paper_result/2rpe_mycalib.zip paper_result/2rpe_online.zip paper_result/2rpe_kalibr.zip -p --save_table paper_result/2rpe_table.csv



##cat traj_estimate.txt | tr -s [:space:] > traj_estimate_new.txt
#rev traj_estimate.txt | cut -d " " -f 13- | rev > mycalib_traj.txt
#rev traj_estimate.txt | cut -d " " -f 13- | rev > kalibr_traj.txt
