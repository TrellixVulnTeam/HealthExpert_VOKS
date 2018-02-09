package com.healthexpert.doctor.fragments;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.healthexpert.R;
import com.healthexpert.admin.activities.AdminDoctorDetailsActivity;
import com.healthexpert.common.BaseFragment;
import com.healthexpert.data.remote.models.response.Doctor;
import com.healthexpert.doctor.adapters.DoctorHomeAdapter;

import java.util.ArrayList;

/**
 * Created by Archish on 1/28/2017.
 */

public class DoctorHomeFragment extends BaseFragment implements DoctorHomeAdapter.LikeItemUpdateListener {

    RecyclerView rvHome;

    @Override
    public void onNetworkException(Throwable e) {
        super.onNetworkException(e);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_patient_home, container, false);
        rvHome = (RecyclerView) view.findViewById(R.id.rvHome);
        rvHome.setHasFixedSize(true);
        rvHome.setLayoutManager(new GridLayoutManager(getActivity().getApplicationContext(), 2, GridLayoutManager.VERTICAL, false));
        fetchData();
        return view;
    }

    public void fetchData() {
        ArrayList<String> data = new ArrayList<>();
        data.add("Patients");
        data.add("Doctor");
        data.add("My Patients");
        data.add("Summary");
        data.add("Profile");
        DoctorHomeAdapter homeAdapter = new DoctorHomeAdapter(data, this);
        rvHome.setAdapter(homeAdapter);

    }


    @Override
    public void onItemCardClicked(Doctor home) {
        Intent i = new Intent(getActivity(), AdminDoctorDetailsActivity.class);
        i.putExtra("doctor", home);
        startActivity(i);
    }
}