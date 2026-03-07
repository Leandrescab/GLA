import streamlit as st
from pathlib import Path
from app.components.file_upload.file_upload_component import FileUploadComponent
from app.components.optimization.optimization_settings import OptimizationSettingsComponent
from app.components.optimization.optimization_history import OptimizationHistoryComponent
from app.components.optimization.optimization_execution import OptimizationExecutionComponent
from backend.entities.database import SnowflakeDB
from backend.services.data_loader_service import DataLoader
from app.utils.state_keys import StateKeys

class OptimizationPage:
    def __init__(self):
        self.db = SnowflakeDB()
        self.file_upload = FileUploadComponent()
        self.loaded_data = None
        self.optimization_settings = OptimizationSettingsComponent()
        self.optimization_execution = OptimizationExecutionComponent(self.db)
        self.optimization_history = OptimizationHistoryComponent(self.db)

    def show(self):
        """
        This method is called by the app to show the optimization page.
        It is called once when the user navigates to the optimization page.
        """
        self.file_upload.show()
        temp_path = st.session_state[StateKeys.SESSION_KEY_TEMP_PATH]
        load_mode = st.session_state[StateKeys.SESSION_KEY_DATA_LOAD_MODE]
        is_data_ready = temp_path is not None and Path(temp_path).exists()
        loader = DataLoader(temp_path)
        if is_data_ready and self.loaded_data is None:
            self.loaded_data = loader.load_data()
        st.divider()
        self._show_tabs(is_data_ready)


    def _show_tabs(self, is_data_ready):
        """
        This method is called by the app to show the tabs.
        It is called once when the user navigates to the optimization page.
        """
        tab1, tab2, tab3 = st.tabs([
            "Constrained Optimization",
            "Global Optimization",
            "Optimization History"
        ])
        with tab1:
            if is_data_ready:
                with st.container():
                    constrained_settings = self.optimization_settings.choose_constrained_settings()
                    self.optimization_execution.run_constrained_optimization(self.loaded_data, constrained_settings)
            else:
                self._show_warning()

        with tab2:
            if is_data_ready:
                with st.container():
                    global_settings = self.optimization_settings.choose_global_settings()
                    self.optimization_execution.run_global_optimization(self.loaded_data, global_settings)
            else:
                self._show_warning()

        with tab3:
            with st.container():
                self.optimization_history.show()
                #self.optimization_history.show_optimization_history()
                #self.optimization_history.show_well_details()



    def _show_warning(self):
        """
        Display a warning banner when no data has been loaded for optimization.
        """
        st.markdown("""
            <div class="banner-warning">
              <span>⚠️</span>
              <div>
                <strong>Please load data first to perform the optimization</strong>
                <div class="banner-warning-text"> Use the "Data Editor" or "Upload Data" tab to load data.</div>
              </div>
            </div>""", unsafe_allow_html=True)