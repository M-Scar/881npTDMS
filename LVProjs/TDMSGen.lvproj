<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="26008000">
	<Property Name="NI.LV.All.SaveVersion" Type="Str">26.0</Property>
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="advancedOpenNoClose.vi" Type="VI" URL="../advancedOpenNoClose.vi"/>
		<Item Name="tdmsGenTool.vi" Type="VI" URL="../tdmsGenTool.vi"/>
		<Item Name="tdmsGenToolAllDAQmxTypes.vi" Type="VI" URL="../tdmsGenToolAllDAQmxTypes.vi"/>
		<Item Name="tdmsGenToolAllDataTypes.vi" Type="VI" URL="../tdmsGenToolAllDataTypes.vi"/>
		<Item Name="tdmsGenToolExtended.vi" Type="VI" URL="../tdmsGenToolExtended.vi"/>
		<Item Name="tdmsGenToolScaleAllDAQmxTypes.vi" Type="VI" URL="../tdmsGenToolScaleAllDAQmxTypes.vi"/>
		<Item Name="tdmsLiveCreation.vi" Type="VI" URL="../tdmsLiveCreation.vi"/>
		<Item Name="tdmsLiveCreationAndDeletion.vi" Type="VI" URL="../tdmsLiveCreationAndDeletion.vi"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="advancedOpenNoClose" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{F94192EA-FD61-4CDF-9B16-A00ED9325ADC}</Property>
				<Property Name="App_INI_GUID" Type="Str">{C8ECF76B-E800-42EE-8DFE-97CE32BCA8D8}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{C21EAE4C-E7D6-49B9-93AB-8B44638F6E62}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">advancedOpenNoClose</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{8D96ED13-F15D-437D-B9C4-931B64F5E4C4}</Property>
				<Property Name="Bld_version.build" Type="Int">3</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">advancedOpenNoClose.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/advancedOpenNoClose.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{1EB67BC5-CD43-4B06-A516-B6B93ED4BBBC}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/advancedOpenNoClose.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">The Pennsylvania State University</Property>
				<Property Name="TgtF_fileDescription" Type="Str">advancedOpenNoClose</Property>
				<Property Name="TgtF_internalName" Type="Str">advancedOpenNoClose</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2026 The Pennsylvania State University</Property>
				<Property Name="TgtF_productName" Type="Str">advancedOpenNoClose</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{04F7E382-7E7B-4E10-923A-CF608A860953}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">advancedOpenNoClose.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="liveTDMSStream" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{99D68374-9B04-45B6-AAEB-87D92A76C4EF}</Property>
				<Property Name="App_INI_GUID" Type="Str">{D7F18C16-5C6B-43EC-A371-02BA251FA6C4}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{FE5A1A71-1B0E-4314-8E6A-D4A5922A80FD}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">liveTDMSStream</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{90A0C4B9-5EBE-47E6-BB57-32923B61A9C4}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">liveTDMSStream.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/liveTDMSStream.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{0A1960D1-DD76-4E10-9631-6D830D2D5D95}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/tdmsLiveCreation.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">The Pennsylvania State University</Property>
				<Property Name="TgtF_fileDescription" Type="Str">liveTDMSStream</Property>
				<Property Name="TgtF_internalName" Type="Str">liveTDMSStream</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2026 The Pennsylvania State University</Property>
				<Property Name="TgtF_productName" Type="Str">liveTDMSStream</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{919A513C-3EE2-48F5-A929-E1F2DF0F6C3F}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">liveTDMSStream.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="My Application" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{454A99A9-104F-4DC5-99F5-475E3D61C5B7}</Property>
				<Property Name="App_INI_GUID" Type="Str">{368ED09C-6992-4AA2-8EB6-4683F88B5FE0}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{8BAC9E69-C827-4369-B213-F5BE14C1647B}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">My Application</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/My Application</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{FD3E0408-8B0E-4915-9166-860EBF33459A}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">tdmsGen.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/tdmsGen.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{1EB67BC5-CD43-4B06-A516-B6B93ED4BBBC}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/tdmsGenTool.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">The Pennsylvania State University</Property>
				<Property Name="TgtF_fileDescription" Type="Str">My Application</Property>
				<Property Name="TgtF_internalName" Type="Str">My Application</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2026 The Pennsylvania State University</Property>
				<Property Name="TgtF_productName" Type="Str">My Application</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{7A8233BF-A3DA-4354-AC82-4B3CA1EA45DD}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">tdmsGen.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
