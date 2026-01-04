#cat 6basalt/traj_estimate.txt | tr -s [:space:] > 6basalt/traj_estimate_new.txt
#rev 6basalt/traj_estimate_new.txt | cut -d " " -f 13- | rev > 6basalt/basalt_traj.txt

cat traj_estimate.txt | tr -s [:space:] > traj_estimate_new.txt
rev traj_estimate_new.txt | cut -d " " -f 13- | rev > mycalib_traj.txt
